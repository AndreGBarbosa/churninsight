package com.one.churninsight;

import com.one.churninsight.business.dto.ChurnRequestDTO;
import com.one.churninsight.business.dto.ChurnResponseDTO;
import com.one.churninsight.business.service.ChurnService;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class ChurninsightApplicationTests {

	@Autowired
	private ChurnService churnService; // Injetamos o serviço que queremos testar

	@Test
	void contextLoads() {
		// Teste padrão do Spring: Só verifica se o app sobe
	}

	@Test
	void testeIntegracaoComPython() {
		System.out.println(">>> Iniciando teste de conexão com a IA...");

		// 1. Preparar o cenário (Dados falsos)
		ChurnRequestDTO clienteTeste = ChurnRequestDTO.builder()
				.months(12.0)
				.rev_Mean(55.0)
				.mou_Mean(180.0)
				.totcalls(40.0)
				.eqpdays(100.0)
				.build();

		// 2. Executar a ação (Chamar o serviço real)
		// ATENÇÃO: O Python precisa estar rodando na janela preta para isso funcionar!
		ChurnResponseDTO resposta = churnService.solicitarPrevisao(clienteTeste);

		// 3. Validar o resultado (O "Assert")
		Assertions.assertNotNull(resposta, "A resposta não deveria ser nula");
		Assertions.assertNotNull(resposta.getPrevisao(), "A previsão não deveria ser nula");

		System.out.println(">>> SUCESSO! A IA respondeu: " + resposta.getPrevisao());
		System.out.println(">>> Probabilidade: " + resposta.getProbabilidade());
	}
}