package com.one.churninsight.controller;

import com.one.churninsight.business.dto.ChurnRequestDTO;
import com.one.churninsight.business.service.ChurnService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/churn")
public class ChurnController {

    @Autowired
    private ChurnService churnService;

    @PostMapping("/analise")
    public ResponseEntity<?> analisar(@RequestBody ChurnRequestDTO dto) {

        // Validação básica: O campo 'months' é obrigatório
        if (dto.getMonths() == null) {
            return ResponseEntity.badRequest().body("Erro: O campo 'months' (tempo de contrato) é obrigatório.");
        }

        try {
            // Chama o serviço
            var resposta = churnService.solicitarPrevisao(dto);
            return ResponseEntity.ok(resposta);

        } catch (Exception e) {
            // Se der erro de conexão com o Python
            return ResponseEntity.internalServerError()
                    .body("Erro: Não foi possível conectar com o serviço de IA. Verifique se o Python está rodando.");
        }
    }
}