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
		System.out.println(">>> Iniciando teste de conexão com a IA (Modelo Expandido)...");

		// 1. Preparar o cenário (Dados falsos preenchendo as 13 colunas)
		ChurnRequestDTO clienteTeste = ChurnRequestDTO.builder()
				// --- Dados Básicos (MVP Antigo) ---
				.months(12.0)
				.rev_Mean(55.5)
				.mou_Mean(200.0)
				.totcalls(45.0)
				.eqpdays(300.0)

				// --- Novos Dados (Engenharia de Features) ---
				.rev_per_minute(0.27)
				.calls_per_month(3.75)
				.eqp_age_index(1.5)

				// --- Novos Dados (Histórico/Suporte) ---
				.custcare_Mean(2.0)
				.drop_vce_Mean(1.0)
				.blck_vce_Mean(0.5)
				.avgmou(190.0)
				.avgrev(50.0)
				.build();

		// 2. Executar a ação (Chamar o serviço real)
		// ATENÇÃO: O Python precisa estar rodando na janela preta (py app.py) para isso funcionar!
		ChurnResponseDTO resposta = churnService.solicitarPrevisao(clienteTeste);

		// 3. Validar o resultado
		Assertions.assertNotNull(resposta, "A resposta não deveria ser nula");
		Assertions.assertNotNull(resposta.getPrevisao(), "A previsão não deveria ser nula");

		System.out.println("------------------------------------------------");
		System.out.println(">>> SUCESSO! Integração Java <-> Python funcionando.");
		System.out.println(">>> Previsão: " + resposta.getPrevisao());
		System.out.println(">>> Probabilidade: " + (resposta.getProbabilidade() * 100) + "%");
		System.out.println("------------------------------------------------");
	}
}