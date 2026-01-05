package com.one.churninsight.business.dto;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ChurnRequestDTO {

    // --- Dados Originais ---
    private Double months;
    private Double rev_Mean;
    private Double mou_Mean;
    private Double totcalls;
    private Double eqpdays;

    // --- Novos Dados (Engenharia de Features) ---
    private Double rev_per_minute;
    private Double calls_per_month;
    private Double eqp_age_index;

    // --- Novos Dados (Brutos) ---
    private Double custcare_Mean; // Chamadas para suporte
    private Double drop_vce_Mean; // Chamadas caídas
    private Double blck_vce_Mean; // Chamadas bloqueadas
    private Double avgmou;        // Média histórica de uso
    private Double avgrev;        // Média histórica de receita
}