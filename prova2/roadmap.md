- [X] Ordenar vetor

- [X] Ler linhas de um arquivo teste e ordenar

- [X] Ler linhas de um arquivo teste imenso e ordenar com limite de 1000 na memoria, checando tamanho do vetor

- [X] Ler linhas de um arquivo teste imenso e armazenar jogando resultados por partes na memoria, com feedback
   - Qual seria esse feedback? Checar o tamanho de todos subvetores para ver se sao mesmo <= a 1000

- [ ] Ordenar os chunks, validar

- [ ] Ordenar todo o conteudo, validar

- [ ] Ler linhas do arquivo teste e jogar para out.txt de 1000 em 1000. O buffer tem tamanho maximo de 1000, mudar isso! Ter feedback
   - Qual seria esse feedback? Processo:
      - limpar arquivo out.txt, se existir
      - criar arquivo out.txt
      - criar novo jeito de bufferizar: objetivo deve ser armazenar os chunks no buffer e fazer o flush em seguida, para o arquivo out.txt
         - validar tamanho do chunk
         - TODO: ...

- [ ] Teste de integracao, com arquivo real lidado pelo codigo principal