## Rish shell

`rish` é um executável Android (não um app) para interagir com um shell que roda em um processo daemon com privilégios elevados.
Por exemplo, se o Shizuku foi iniciado com privilégios de ADB, o `rish` também fornecerá um shell que mantém os privilégios de ADB.

Para configurar o `rish`, abra o Shizuku, vá até 'Usar o Shizuku em apps de terminal' e siga as instruções de configuração. Observe que você precisa de um conhecimento básico de shells, terminais e comandos essenciais para usá-lo com eficiência.

Depois de configurar o `rish`, você pode usá-lo junto com qualquer app que permita chamar scripts de shell ou executáveis, mesmo que o app não tenha suporte ao Shizuku.

> [!NOTE]
> Como o local do `rish` não está no `$PATH`, talvez seja necessário especificar o caminho do executável para iniciá-lo manualmente. Se ele estiver no seu diretório de trabalho atual, use `./rish` para iniciá-lo.

**Sintaxe:**

* `rish`: Inicia o shell interativo padrão (usa /system/bin/sh)
* `rish exec /path/to/custom/shell`: Inicia um shell interativo personalizado/alternativo
* `rish -c 'whoami'`: Executa o comando de shell e sai ao terminar
* `echo 'whoami' | rish`: Lê o comando de shell do stdin, executa-o e sai ao terminar

> [!NOTE]
> `whoami` é usado como comando de exemplo e retorna o nome do usuário atual do shell.

**Exemplos de uso:**

* Abrir um shell ADB interativo usando um emulador de terminal como o **Termux** diretamente no dispositivo
* Disparar comandos de shell ADB de alto privilégio automaticamente em segundo plano usando apps de automação como o **Tasker**
  * Exemplo: o comando `rish -c 'reboot'` reiniciaria o dispositivo usando o Shizuku via shell

A documentação oficial do rish está disponível aqui: https://github.com/RikkaApps/Shizuku-API/blob/master/rish/README.md
