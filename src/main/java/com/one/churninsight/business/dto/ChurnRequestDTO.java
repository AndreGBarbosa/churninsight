package com.one.churninsight.business.dto;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ChurnRequestDTO {

    private Long tempoContratoMeses;
    private Long atrasoPagamentos;
    private Double usoMensal;
    private String plano;
}
