package com.example.gestionuser.service;

import com.example.gestionuser.entity.User;
import com.example.gestionuser.repository.IUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class GestionUserImpl implements IGestionUser {
    @Autowired
    private IUserRepository userRepository;

    @Override
    public User addUser(User u) {
        return userRepository.save(u);
    }
}