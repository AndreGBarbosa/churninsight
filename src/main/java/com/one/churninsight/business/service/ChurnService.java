package com.one.churninsight.business.service;

import com.one.churninsight.business.dto.ChurnRequestDTO;
import com.one.churninsight.business.dto.ChurnResponseDTO;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class ChurnService {

    public ChurnResponseDTO solicitarPrevisao(ChurnRequestDTO dadosCliente) {
        // 1. URL do Python (que deve estar rodando na tela preta)
        String urlPython = "http://localhost:5000/predict";

        // 2. O Carteiro (RestTemplate)
        RestTemplate carteiro = new RestTemplate();

        // 3. Envia o ChurnRequestDTO e recebe o ChurnResponseDTO
        // Graças ao Lombok, o Java faz a conversão do JSON automaticamente
        return carteiro.postForObject(urlPython, dadosCliente, ChurnResponseDTO.class);
    }
}