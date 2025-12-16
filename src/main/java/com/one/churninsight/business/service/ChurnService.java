package com.one.churninsight.business.service;

import com.one.churninsight.business.dto.ChurnRequestDTO;
import com.one.churninsight.business.dto.ChurnResponseDTO;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
@AllArgsConstructor
public class ChurnService {

    private final RestTemplate restTemplate;

    public ChurnResponseDTO prever(ChurnRequestDTO request) {

        String url = "http://localhost:8000/predict";

        return restTemplate.postForObject(
                url,
                request,
                ChurnResponseDTO.class
        );
    }
}
