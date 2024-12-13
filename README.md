# Bot-bate-ponto
Este é um bot para Discord que ajuda a monitorar e controlar o tempo de trabalho. O bot permite que os usuários iniciem e finalizem o controle de ponto, enviando mensagens detalhadas com o horário de início, horário de saída e o tempo total trabalhado.

# Funcionalidades
Iniciar Ponto: Comando !iniciar para começar a contar o tempo.

Finalizar Ponto: Botão "Finalizar" para encerrar o ponto e calcular o tempo total trabalhado.
Mensagens Embutidas: Mensagens com horários e tempo total em formato amigável.

Instalação:
1- Clone o repositório
2- Instale as dependências

Configuração:

1- Substitua DISCORD_TOKEN pelo token do seu bot Discord.
2- Defina o TARGET_CHANNEL_ID com o ID do canal onde as mensagens de ponto finalizado serão enviadas.

Comandos:
!iniciar: Inicia o controle de ponto. Se o ponto já estiver em andamento, mostra a hora de início e a mensagem apropriada.

Exemplo de Uso
Iniciar Ponto:

O usuário envia !iniciar no canal do Discord. O bot responde com uma mensagem embutida informando o horário de início e exibe um botão "Finalizar".

Finalizar Ponto:

O usuário clica no botão "Finalizar". O bot envia uma mensagem com o horário de início, horário de saída e o tempo total trabalhado.

Detalhes Técnicos

Biblioteca: discord.py
Intents: Configuração para receber conteúdo de mensagens.
Botões Interativos: Utiliza discord.ui.View e discord.ui.Button para a interação.

Contribuição
Sinta-se à vontade para enviar pull requests ou reportar problemas. Agradeço sua colaboração!
