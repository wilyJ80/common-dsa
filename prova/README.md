Editor de texto: Imagine que você foi encarregado de desenvolver um aplicativo de editor de
texto simples que suporte as seguintes funcionalidades:

1. Operação de desfazer (usando uma pilha). Pode ser feita várias vezes.

2. Operação de refazer (usando uma pilha). Pode ser feita o mesmo número de vezes que o undo foi feito

3. Processamento de uma série de edições de texto

Detalhes:

1. Arquivo de Edições de Texto: O arquivo edits.txt contém uma série de comandos de edição de texto (adicionar, deletar, substituir, desfazer, refazer) no formato:

2. Exibição dos resultados: Após cada comando, imprima o resultado atual do texto no terminal.

3. Proponha um comando novo e implemente no código [0.5 pontos]

4. Critérios: o resultado final será comparado com o resultado desejado linha e a linha e o código também será avaliado por boas práticas

Comando | Funcionalidade
--- | ---
add string | adiciona string no final do texto
replace tamanho string | remove tamanho caracteres e adiciona string a partir do final do texto
delete tamanho | Remove tamanho caracteres do final do texto
undo | Desfaz a ultima acao
redo | Refaz a ultima acao


