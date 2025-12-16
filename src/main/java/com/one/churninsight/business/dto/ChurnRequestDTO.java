package com.one.churninsight.business.dto;

import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.PositiveOrZero;
import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ChurnRequestDTO {

    @NotNull
    @PositiveOrZero
    private Long tempoContratoMeses;

    @NotNull
    @PositiveOrZero
    private Long atrasoPagamentos;

    @NotNull
    @PositiveOrZero
    private Double usoMensal;

    @NotNull
    private String plano;
}
