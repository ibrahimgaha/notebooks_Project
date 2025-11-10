from django.apps import AppConfig
import os
import asyncio
import threading
import requests
from py_eureka_client.eureka_client import EurekaClient

class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        # Initialize Eureka client when Django starts
        eureka_client = EurekaClient(
            eureka_server="http://localhost:8761/eureka",
            app_name="PRODUCTSMANAGEMENT",
            instance_host="localhost",
            instance_port=8000,
            instance_id="PRODUCTSMANAGEMENT:8000",
        )

        # Start Eureka registration in a separate thread
        def register_with_eureka():
            try:
                # Manual registration as fallback
                instance_data = {
                    "instance": {
                        "instanceId": "PRODUCTSMANAGEMENT:8000",
                        "hostName": "localhost",
                        "app": "PRODUCTSMANAGEMENT",
                        "ipAddr": "127.0.0.1",
                        "status": "UP",
                        "port": {"$": 8000, "@enabled": "true"},
                        "securePort": {"$": 443, "@enabled": "false"},
                        "healthCheckUrl": "http://localhost:8000/health/",
                        "statusPageUrl": "http://localhost:8000/status/",
                        "homePageUrl": "http://localhost:8000/",
                        "dataCenterInfo": {
                            "@class": "com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo",
                            "name": "MyOwn"
                        }
                    }
                }

                # Try manual registration first
                response = requests.post(
                    "http://localhost:8761/eureka/apps/PRODUCTSMANAGEMENT",
                    json=instance_data,
                    headers={"Content-Type": "application/json"}
                )

                if response.status_code == 204:
                    print("Django service registered with Eureka successfully (manual)")
                else:
                    # Fallback to library method
                    asyncio.run(eureka_client.register())
                    print("Django service registered with Eureka successfully (library)")

            except Exception as e:
                print(f"Failed to register Django service with Eureka: {e}")

        thread = threading.Thread(target=register_with_eureka)
        thread.daemon = True
        thread.start()
