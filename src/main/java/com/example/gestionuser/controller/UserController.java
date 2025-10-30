package com.example.gestionuser.controller;

import com.example.gestionuser.entity.User;
import com.example.gestionuser.service.IGestionUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/User")
public class UserController {
    private final IGestionUser serviceUser;

    @Autowired
    public UserController(IGestionUser serviceUser) {
        this.serviceUser = serviceUser;
    }

    @PostMapping("/addUser")
    public User addClient(@RequestBody User u) {
        return serviceUser.addUser(u);
    }
}