package com.one.churninsight.controller;

import com.one.churninsight.business.dto.ChurnRequestDTO;
import com.one.churninsight.business.dto.ChurnResponseDTO;
import com.one.churninsight.business.service.ChurnService;
import jakarta.validation.Valid;
import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/churn")
@AllArgsConstructor
public class ChurnController {

    private final ChurnService churnService;

    @PostMapping("/prever")
    public ChurnResponseDTO prever(@Valid @RequestBody ChurnRequestDTO request) {
        return churnService.prever(request);
    }
}
