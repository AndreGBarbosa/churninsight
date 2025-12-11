package com.one.churninsight.business.dto;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class ChurnResponseDTO {

    private String previsao;
    private Double probablidade;
}
