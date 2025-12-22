package com.one.churninsight.business.dto;

import lombok.*;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ChurnRequestDTO {

    // Precisamos usar os nomes EXATOS que o Python espera.
    // Se quiser usar nomes em português, teríamos que usar anotação @JsonProperty("months")
    // Mas para o Hackathon, mudar o nome da variável é mais rápido e seguro.

    private Double months;    // Tempo de contrato
    private Double rev_Mean;  // Receita média
    private Double mou_Mean;  // Média de uso (minutos)
    private Double totcalls;  // Total de chamadas
    private Double eqpdays;   // Idade do equipamento (dias)
}