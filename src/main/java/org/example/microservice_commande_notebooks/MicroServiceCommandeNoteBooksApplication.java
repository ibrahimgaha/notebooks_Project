package org.example.microservice_commande_notebooks;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;

@SpringBootApplication
@EntityScan(basePackages = {"entities"})

public class MicroServiceCommandeNoteBooksApplication {

    public static void main(String[] args) {
        SpringApplication.run(MicroServiceCommandeNoteBooksApplication.class, args);
    }

}
