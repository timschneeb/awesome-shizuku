# awesome-shizuku

### Idiomas
[English](/README.md) | [简体中文](/README_cn.md) | [繁體中文](/README_tw.md) | Português (Brasil)

[![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

O Shizuku permite que apps comuns usem APIs do sistema diretamente, com privilégios elevados, por meio do ADB em dispositivos sem root. Esta lista reúne alguns apps que sabidamente aproveitam os recursos do Shizuku.

Mais detalhes: https://shizuku.rikka.app/

Pull requests são bem-vindos. Veja [Contribuindo](CONTRIBUTING.md) para dicas. Apps de código fechado ficam listados em um arquivo separado. Veja [abaixo](#closed-source-apps) para detalhes.

> [!NOTE]
> Para acompanhar as atualizações desta lista, [você pode conferir os changelogs diários](https://github.com/timschneeb/changelog-awesome-shizuku).

<table>
  <tr>
    <td>
      <h2>Loja de apps para apps Shizuku</h2>   
      <p>
      Esta lista agora está disponível como uma loja de apps de código aberto para Android chamada ShizuStore.<br/>
        <a href="https://github.com/timschneeb/ShizuStore">Downloads e código-fonte estão disponíveis no GitHub.</a>
      </p>
      Você pode navegar por todos os apps Shizuku por categoria, ordenar por adicionados recentemente, número de estrelas no GitHub, downloads ou data de atualização, e instalar ou atualizar APKs silenciosamente pelo Shizuku. 
      Os APKs são baixados direto do desenvolvedor oficial via GitHub, GitLab, F-Droid e outras fontes.
      <br><br>
      <a href="https://github.com/timschneeb/ShizuStore"><img src="https://raw.githubusercontent.com/Kunzisoft/Github-badge/main/get-it-on-github.png" width="240" alt="Disponível no GitHub"></a>
    </td>
    <td align="right">
      <img src="https://raw.githubusercontent.com/timschneeb/ShizuStore/master/fastlane/metadata/android/en-US/images/phoneScreenshots/2.png" width="800" alt="Navegue pelos apps Shizuku por categoria">
    </td>
  </tr>
</table>

--------------------


## Índice

- [Apps](#apps)
  - [Shizuku implementations](#shizuku-implementations)
  - [AI agents](#ai-agents)
  - [Android Auto](#android-auto)
  - [Android TV](#android-tv)
  - [Audio](#audio)
  - [Automation](#automation)
  - [Communication](#communication)
  - [Customization](#customization)
  - [Development utilities](#development-utilities)
  - [Device Owner (DPM)](#device-owner-dpm)
  - [Display management](#display-management)
  - [Entertainment](#entertainment)
  - [File management](#file-management)
  - [Games](#games)
  - [Input methods](#input-methods)
  - [Installer & app stores](#installer--app-stores)
  - [Miscellaneous](#miscellaneous)
  - [Network](#network)
  - [Patching](#patching)
  - [Power management](#power-management)
  - [Privacy](#privacy)
  - [Productivity](#productivity)
  - [Quick settings](#quick-settings)
  - [Software management](#software-management)
  - [Task manager](#task-manager)
  - [Terminals](#terminals)
  - [Vendor-specific](#vendor-specific)
    - [AYN](#ayn)
    - [Google Pixel](#google-pixel)
    - [Samsung OneUI](#samsung-oneui)
    - [MIUI](#miui)
    - [Nothing Phone](#nothing-phone)
    - [Other](#other)
  - [Closed-source apps](#closed-source-apps)
  - [Unlisted apps](#unlisted-apps)
- [Development libraries](#development-libraries)
  - [Core](#core)
  - [Filesystem](#filesystem)
  - [System](#system)
  - [Power](#power)
- [Miscellaneous content](#miscellaneous-content)
- [Rish shell](#rish-shell)
- [Annotations](#annotations)
- [License](#license)

--------------------

## Apps

### Shizuku implementations

> [!NOTE]
> O app oficial do Shizuku, da RikkaApps, não é atualizado há mais de um ano e atualmente não funciona no Android 17.
> Abaixo, você encontra forks do Shizuku com novos recursos e correções.
> 
> Desinstale sua versão atual do Shizuku antes de instalar qualquer uma das alternativas abaixo; caso contrário, você pode ter conflitos de instalação.

* [Porter](https://github.com/d4rken-org/porter) - Fork mínimo e mantido do Shizuku que dá aos apps acesso ADB com root opcional, além de um app complementar de compatibilidade para apps que só suportam Shizuku `Apache-2.0`
* [shevery](https://github.com/HmnDev-Tech/shevery) ✨ - Fork em Material 3 com início automático, modo TCP, Dhizuku, suporte a módulos e um terminal embutido com integração de IA `Apache-2.0`
* [Shizako](https://github.com/cr1437/Shizako) - Edição do Shizuku com mascote catgirl, um gerenciador substituto direto ao qual os apps da API oficial do Shizuku se conectam sem modificação (com recursos parecidos com os do shevery) `Apache-2.0`
* [Shizuku (thedjchi's fork)](https://github.com/thedjchi/Shizuku) - Fork do Shizuku com início automático, modo TCP e modo furtivo (manutenção pausada no momento) `Apache-2.0`
* [Shizuku Next](https://github.com/rushiranpise/Shizuku-Next) - Continuação mantida do fork de thedjchi: pareamento automático sem digitar, escolha do método de inicialização, watchdog, terminal shell no app, gerenciador de app-ops/firewall e interface em Material 3 `Apache-2.0`
* [ShizukuPlus](https://github.com/thejaustin/ShizukuPlus) - Fork do Shizuku com uma API ampliada para desenvolvedores, início automático, modo TCP, Dhizuku e mais `Apache-2.0`
* [Stellar](https://github.com/roro2239/Stellar/blob/main/README_en.md) - Outra implementação do Shizuku com início automático, modo TCP e um terminal simples (pode executar comandos automaticamente na inicialização) `MPL-2.0`
* [Xhizuku](https://github.com/xeonleonreal/Xhizuku) - Fork mantido do Shizuku com interface Material 3 Expressive, executor de módulos ADB, assistente de configuração inicial, monitor do servidor e diagnóstico embutido `Apache-2.0`

### AI agents

* [Aether](https://github.com/Zhou-Shilin/Aether) - Agente de IA de uso geral, localizado e extensível, para Android, iOS e macOS, com integração opcional com Shizuku e Termux para controle direto do dispositivo. `GPL-3.0`
* [AndroidHarness](https://github.com/Sanuu7/AndroidHarness) - Agente de programação no dispositivo que encaminha comandos privilegiados por um UID de shell do Shizuku, com um conjunto de ferramentas Linux com prefixo do Termux como alternativa. `MIT`
* [AutoXiao'er](https://github.com/Joy-word/AutoXiaoer) - Agente de IA no dispositivo que opera apps Android visualmente, com gatilhos de tarefas agendadas, por notificação e via ClawBot. Suporta controle tanto pelo Shizuku quanto por acessibilidade. `MIT`
* [ClawGUI](https://github.com/ZJU-REAL/ClawGUI) - Executor de agente de interface gráfica no dispositivo que roda toda a pilha "cérebro" do ClawGUI em um único celular controlado via Shizuku. `Apache-2.0`
* [DeepSeek Harness for Android](https://github.com/guzhou079-arch/deepseek-harness-android) - Empacota o runtime de agente DeepSeek Harness e 21 skills incluídas em um APK, sem precisar de Termux ou root. O Shizuku alimenta o shell privilegiado, o controle de apps e a automação de tela virtual; o app também consegue compilar e assinar o próprio APK no dispositivo. `MIT`
* [Hermes Agent](https://github.com/adybag14-cyber/hermes-agent) - Port do Hermes Agent para Android com uma ponte de shell privilegiado do Shizuku para ações no dispositivo. `MIT`
* [OmniBot](https://github.com/omnimind-ai/OmniBot) - Agente de IA no dispositivo com terminal, navegação web, controle do dispositivo e integração com o sistema `GPL-3.0`
* [Open-AutoGLM-Android](https://github.com/xinzezhu/Open-AutoGLM-Android/blob/main/README_EN.md) - Automatiza ações no seu dispositivo usando o modelo de linguagem visual AutoGLM `GPL-3.0`
* [OpenCyvis](https://github.com/opencyvis/opencyvis-phone) - Celular com IA de código aberto que vê sua tela e opera apps a partir de tarefas em linguagem natural, funciona em segundo plano `Apache-2.0`
* [OpenDroid](https://github.com/yashab-cyber/opendroid) - Agente de IA autônomo de código aberto no dispositivo que planeja e executa tarefas de várias etapas por automação de tela `Apache-2.0`
* [OpenMinis](https://github.com/OpenMinis/OpenMinis) - Agente com IA com shell Linux, automação de navegador e controle do sistema via Shizuku `GPL-3.0`
* [Operit AI](https://github.com/AAswordman/Operit) - O agente de IA e software de chat com IA mais poderoso do Android. Pode executar comandos usando o Shizuku `LGPL-3.0`
* [rish-mcp](https://github.com/turin-dev/rish-mcp) - Expõe o shell do Shizuku de um dispositivo Android para IAs como uma ferramenta MCP `run_shell` por meio de um relay WebSocket de saída: execute comandos shell a partir do Claude ou de qualquer cliente MCP sem VPN, ADB ou sshd `MIT`
* [roubao](https://github.com/Turbo1123/roubao/blob/main/README_EN.md) - Assistente de automação de celular com IA de código aberto, no dispositivo, baseado em modelos de linguagem visual, que executa tarefas usando permissões de sistema do Shizuku, sem precisar de PC. `MIT` [(Código-fonte)](https://github.com/Turbo1123/roubao)
* [Ruto-GLM](https://github.com/iamr0s/Ruto-GLM/blob/main/README_en.md) - Framework de automação e multitarefa usando o AutoGLM. Pode criar telas virtuais nas quais os agentes executam apps e usam várias janelas `Apache 2.0`
* [talon](https://github.com/thefalconry/talon) - Harness de IA agêntica multiplataforma para Telegram/Discord/Teams/terminal com um app complementar em Flutter; o Shizuku permite autoatualizações silenciosas e acesso elevado. `Apache-2.0`
* [Verdroid](https://github.com/chr243/Verdroid) - Agente de IA no dispositivo ajustado para modelos gratuitos do OpenRouter/Kilo, com ferramentas do Termux, acesso ao shell Shizuku/rish, controle por acessibilidade e tradução de ebooks/PDFs. `GPL-3.0`
* [Virtual Screen](https://github.com/lejw0925/android-virtual-screen/blob/main/README.en.md) - Gives an AI agent its own Android display to launch and operate apps on while you keep using the main screen, with an on-phone MCP server, PiP progress and take-over control `PolyForm-Noncommercial-1.0.0`
* [Zafiro](https://github.com/niki914/zafiro) - Agente de IA no estilo "traga sua própria chave" que lê a tela e controla o dispositivo pelo Shizuku, sem root. `MIT`

### Android Auto

* [Flywheel](https://github.com/Benjamin-Wiegand/Flywheel) - Alternativa livre e de código aberto ao Android Auto voltada a celulares sem Google, compatível com centrais multimídia existentes; o Shizuku é usado para incorporar apps e capturar o áudio de chamadas. `GPL-3.0`

### Android TV

* [flicky](https://apt.izzysoft.de/fdroid/index/apk/app.flicky) - Um cliente F-Droid feito para Android TVs `GPL-3.0` [(Código-fonte)](https://github.com/mlm-games/flicky)
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - Gerenciador de arquivos e visualizador de arquivos compactados com suporte a Android TV. Permite acesso total aos arquivos usando o Shizuku, se ativado nas configurações `GPL-3.0` [(Código-fonte)](https://github.com/mlm-games/fluffy)
* [RecentAppsTV](https://github.com/Qutaiba-Khader/RecentAppsTV) - Overlay de apps recentes para Android TV `Propietary`
* [TVPilot](https://github.com/mahmutaunal/TVPilot) - Controle do sistema e gerenciamento de apps pensados para o controle remoto em Android TV / Google TV, com ações avançadas opcionais via Shizuku `Apache-2.0`

### Audio

* [allEQ](https://github.com/omixin/allEQ) - Equalizador de sistema de 10 bandas sem root que se conecta à sessão de áudio da mixagem de saída pelo Shizuku. `GPL-3.0`
* [android-realtime-voice-isolation](https://github.com/sk2andy/android-realtime-voice-isolation) - Isolamento de voz em tempo real no dispositivo usando Shizuku, GTCRN e ONNX Runtime `MIT`
* [Castix](https://github.com/elhizazi1/Castix) - Gerencia restrições de reprodução em segundo plano e adiciona um relógio em tela preta AMOLED, com backends Shizuku, Dhizuku, root, LSPosed ou acessibilidade. `GPL-3.0`
* [centuryplay](https://github.com/g8row/centuryplay) - Transmite o áudio do sistema Android para alto-falantes AirPlay 1/2; o modo Shizuku opcional permite captura com o celular em silêncio via loopback do AudioPolicy e elimina os avisos de captura. `AGPL-3.0`
* [finevolume](https://github.com/broknhrt2562/finevolume) - Painel de volume no estilo Pixel com precisão de 120 níveis, além de controle de volume por app e por fluxo, usando um proxy de áudio de alta precisão do Shizuku. `Apache-2.0`
* [MicUp](https://github.com/papergray/MicUp) ✨ - Processamento de áudio do microfone em tempo real para Android `MIT`
* [Mixer (1)](https://github.com/farizanjum/mixer-1) - Overlay de volume por app que intercepta os botões físicos `Proprietary`
* [RootlessJamesDSP](https://play.google.com/store/apps/details?id=me.timschneeberger.rootlessjamesdsp) - Uma implementação do mecanismo de processamento de áudio JamesDSP para todo o sistema em dispositivos Android sem root `GPL-3.0` [(Código-fonte)](https://github.com/timschneeb/RootlessJamesDSP)
* [Spotify Ad Skipper](https://github.com/sihooney/spotify-ad-skipper) - Monitora as notificações do Spotify e pula anúncios automaticamente reiniciando a reprodução, usando o Shizuku para reabrir o app em segundo plano. `Proprietary`
* [Volume++](https://github.com/noel-digital-fan/volume_plus_plus) ✨ - Painel de volume personalizado com mixagem de áudio por app via Shizuku ou root `MIT`
* [VolumeManager](https://github.com/yume-chan/VolumeManager) - Controle o volume de cada app de forma independente `GPL-2.0`
* [wecho](https://github.com/qumolangmo/wecho) - Um app Android para processamento global de efeitos de áudio `GPL-3.0`

### Automation

* [Airplane Scheduler](https://f-droid.org/packages/io.github.probecat.airplanescheduler/) - Turns airplane mode on and off on a schedule so your phone goes quiet at night, with overnight ranges, optional Wi-Fi toggling `GPL-3.0` [(Código-fonte)](https://github.com/probecat/airplane-scheduler-app)
* [Argus](https://github.com/JackRushante/argus) - Automação Android no nível do Tasker, em que um LLM compila regras em linguagem natural para um mecanismo determinístico, com um gateway opcional de shell do Shizuku. `GPL-3.0`
* [AutoJs6](https://github.com/SuperMonster003/AutoJs6) - Ferramenta de automação baseada em JavaScript `MPL-2.0`
* [AutoSlide](https://github.com/tianxing-ovo/AutoSlide/blob/master/README.en.md) - Ferramenta de rolagem automática que reproduz vídeos curtos e vira páginas de leitura sozinha, com controles flutuantes `Apache-2.0` [(Código-fonte)](https://github.com/tianxing-ovo/AutoSlide)
* [flowpilot](https://github.com/emi-ran/flowpilot) - Mecanismo de automação offline com foco em privacidade que executa ações privilegiadas do sistema, como dados móveis, modo avião e tema escuro, pelo Shizuku. `GPL-3.0`
* [IMD](https://github.com/soul-99/SU_IMD) ✨ - Fork do Geto que oculta as opções do desenvolvedor, o ADB, os serviços de acessibilidade e o próprio Shizuku de apps restritivos, como os de banco, e depois os restaura `GPL-3.0`
* [Latch](https://github.com/wized2/Latch) - Privacy-first Tasker-style automation with local if/then rules, multi-action chains, optional Shizuku/root elevated actions, and no cloud. `MIT`
* [NexaFlow](https://github.com/Alaa91H/NexaFlow) - Mecanismo de automação Android sensível ao contexto que combina gatilhos, restrições e ações, com execução via Shizuku para controles privilegiados do dispositivo. `MIT`
* [Nothing_Modes](https://github.com/Dvorinka/Nothing_Modes) - App de automação para celulares Nothing (modos, rotinas, Glyph) que também funciona em outros dispositivos Android com Shizuku opcional `GPL-3.0`
* [OpenTasker](https://github.com/SysAdminDoc/OpenTasker) - Alternativa ao Tasker de código aberto e local em primeiro lugar, com regras legíveis e controles de permissão transparentes; ações privilegiadas rodam por um serviço de usuário AIDL do Shizuku. `MIT`
* [PhoneProfilesPlus](https://github.com/henrichg/PhoneProfilesPlus) - Permite configurar o dispositivo automaticamente ou com um toque para situações específicas do dia a dia `Apache-2.0`
* [Service-Keeper](https://github.com/sklndev/Service-Keeper) - Monitora serviços em segundo plano, de acessibilidade e de leitura de notificações e reinicia automaticamente os que o sistema encerrar. `GPL-3.0`
* [Tasker Settings](https://github.com/joaomgcd/TaskerSettings) - App auxiliar para o Tasker `Propietary`
* [vFlow](https://github.com/ChaoMixian/vFlow/blob/master/README_EN.md) ✨ - Ferramenta de automação visual que combina toques, reconhecimento, ramificações e ações do sistema em fluxos de trabalho acessíveis `GPL-2.0`

### Communication

* [Aliucord-Manager](https://github.com/Aliucord/Manager) - Ferramenta de modificação do Discord `OSL-3.0`
* [Bluesky Redirect](https://apt.izzysoft.de/fdroid/index/apk/io.github.turtlepaw.blueskyredirect) - Um app simples para abrir automaticamente links do Bluesky no seu cliente Bluesky preferido `MIT` [(Código-fonte)](https://github.com/Turtlepaw/BlueskyRedirect)
* [CallVault](https://github.com/madkongo/CallVault) - Gravador de chamadas sem root com transcrições/resumos no dispositivo; autônomo via ADB embutido ou por um backend Shizuku opcional. `GPL-3.0`
* [cally](https://github.com/LyoSU/cally) - Gravador de chamadas para Pixel 6+ de fábrica que captura os dois lados da chamada por um serviço de áudio com UID de shell do Shizuku, sem root nem bootloader desbloqueado. `GPL-3.0`
* [CatShare](https://f-droid.org/packages/moe.reimu.catshare/) - Envie e receba arquivos por Bluetooth `MIT` [(Código-fonte)](https://github.com/kmod-midori/CatShare)
* [ClipShare](https://clipshare.coclyun.top/) - Sincronização de área de transferência multiplataforma para texto, imagens, arquivos e SMS; o Shizuku mantém o monitor da área de transferência do Android em execução. `GPL-3.0` [(Código-fonte)](https://github.com/aa2013/ClipShare/blob/master/README_EN.md)
* [GhostMode](https://github.com/Foxlape/GhostMode) - Faz o celular parecer indisponível para chamadas recebidas enquanto mantém os dados LTE/5G ativos `Apache-2.0`
* [KDE Connect (Shizuku)](https://github.com/Batestinha/kdeconnect-android-shizuku) - Fork não oficial do KDE Connect que adiciona sincronização automática da área de transferência em segundo plano no Android 10+ via Shizuku e callbacks AIDL. `GPL-2.0`
* [KettuManager](https://github.com/C0C0B01/KettuManager) - Ferramenta de modificação do Discord. Continuação do projeto abandonado BunnyManager `OSL-3.0`
* [Lemmy Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.lemmyredirect) - Um app simples para abrir automaticamente links do Lemmy no seu cliente Lemmy preferido. `MIT` [(Código-fonte)](https://github.com/zacharee/MastodonRedirect)
* [Mastodon Redirect](https://apt.izzysoft.de/fdroid/index/apk/dev.zwander.mastodonredirect) - Um app simples para abrir automaticamente links do fediverso no seu cliente Mastodon preferido. `MIT` [(Código-fonte)](https://github.com/zacharee/MastodonRedirect)
* [revenge-manager](https://github.com/revenge-mod/revenge-manager) - Ferramenta de modificação do Discord. Outra continuação do projeto abandonado Bunny-Manager `OSL-3.0`
* [RivoPhoneApp](https://github.com/user-grinch/RivoPhoneApp) - App de discador e contatos em Material 3 com gravação de chamadas via Shizuku, sem root `GPL-3.0`
* [ShizuCallRecorder](https://github.com/kitsumed/ShizuCallRecorder) ✨ - O ShizuCallRecorder usa o ADB pelo Shizuku para gravar chamadas telefônicas em dispositivos sem root! `GPL-3.0`
* [TxtNet-Browser](https://github.com/lukeaschenbrenner/TxtNet-Browser) - Um app que permite navegar na web por SMS `GPL-3.0`

### Customization

* [Adaptive-Theme](https://play.google.com/store/apps/details?id=dev.lexip.hecate) - Modo escuro inteligente baseado na luz ambiente `GPL-3.0` [(Código-fonte)](https://github.com/xLexip/Adaptive-Theme)
* [AmbientMusicMod](https://github.com/KieronQuinn/AmbientMusicMod) - Port do Tocando agora (Now Playing) dos Pixels para outros dispositivos Android `GPL-3.0`
* [android-perapp-language-selector](https://github.com/TakeruF/android-perapp-language-selector) - Força configurações de idioma por app no Android 13+ sem root, mesmo em apps sem opções de idioma próprias `Apache-2.0`
* [AutoDND](https://f-droid.org/packages/moe.dic1911.autodnd/) - Uma ferramenta simples para ativar o Não perturbe automaticamente ao usar apps específicos `AGPL-3.0` [(Código-fonte)](https://github.com/im030/android_AutoDND)
* [AutoRotate](https://github.com/eiyooooo/AutoRotate) - Gerencia a rotação automática de diferentes telas em celulares Android `GPL-3.0`
* [BlackOut](https://github.com/xUmutKx/BlackOut) - Turns grey dark-mode surfaces into true AMOLED black with per-app color rules and force-dark. Shizuku only enables force-dark; root and LSPosed are needed for full functionality `Proprietary`
* [Capsulyric](https://github.com/FrancoGiudans/Capsulyric) - Exibe a letra da música em reprodução na barra de status e na tela de bloqueio via Android Live Update e Xiaomi Super Island `GPL-3.0`
* [CarrierVanityName](https://github.com/nullbytepl/CarrierVanityName) - O Carrier Vanity Name é um app bem simples para alterar o nome da operadora em dispositivos Android sem root `GPL-3.0`
* [XGesture](https://github.com/qpst4/XGesture) - Pacote completo de gestos e navegação com uma mão, com painéis laterais, cursor flutuante, bola de OCR offline, congelador de apps e janelas flutuantes via Shizuku. `AGPL-3.0`
* [CleanBar](https://github.com/sachinmandawi/CleanBar) - Oculta com 1 toque a barra de status e os ícones do sistema, escondendo relógio, bateria e ícones, sem precisar de root `MIT`
* [ColorBlendr](https://github.com/Mahmud0808/ColorBlendr) ✨ - Um app para modificar as cores Material You do seu dispositivo `GPL-3.0`
* [Commander](https://github.com/astroboii47/Commander) - Barra de comandos e central de notificações focadas no teclado; usa o Shizuku para alternar entre apps recentes e para controles privilegiados de shell. `MIT`
* [CustomAnimator](https://play.google.com/store/apps/details?id=com.arslan.customanimator) - Personalize as velocidades de animação com ajuste mais fino `GPL-3.0` [(Código-fonte)](https://github.com/AhmetCanArslan/CustomAnimator)
* [DarQ-Reborn](https://github.com/Arora-Sir/DarQ-Reborn) - Opção de forçar modo escuro selecionável por app para Android 10 e superior `Apache-2.0`
* [Dawn-Desktop-Addons](https://github.com/Dawncraft/Dawn-Desktop-Addons) - Alguns widgets de app e papéis de parede animados para Android `GPL-3.0`
* [DevBay-Launcher](https://github.com/Zoder-Studio/DevBay-Launcher) - Launcher voltado a desenvolvedores, com seções de apps de depuração, pastas, gestos e atalhos rápidos para opções do desenvolvedor, animações, fontes e ADB sem fio via Shizuku. `GPL-3.0`
* [Dragon-Launcher](https://f-droid.org/packages/org.elnix.dragonlauncher/) ✨ - Launcher Android altamente personalizável e baseado em gestos, focado em velocidade e eficiência `GPL-3.0` [(Código-fonte)](https://github.com/Elnix90/Dragon-Launcher)
* [DroidOS](https://github.com/Katsuyamaki/DroidOS) ✨ - Gerenciador de janelas lado a lado (tiling), substituto do Samsung DEX, launcher de apps em pop-up `Proprietary`
* [duo-open](https://github.com/marcoazeem/duo-open) - Efeito de dobra em vidro fosco no estilo iPhone Duo para todo o sistema em dobráveis tipo livro, guiado pelo ângulo real da dobradiça, como overlay de acessibilidade ou papel de parede animado, com Shizuku opcional. `MIT`
* [DuoFold-Android](https://github.com/jcx396905-gif/DuoFold-Android) - Ilusão de dobra no estilo iPhone Duo para todo o sistema que reprojeta a tela inteira a partir do movimento do dispositivo com OpenGL ES, usando o Shizuku. `MIT`
* [EdgeGesture](https://github.com/Evilgodxu/EdgeGesture) - App de gestos de borda baseado em acessibilidade e Shizuku: deslizes na borda, toque na traseira, painéis flutuantes de música e tarefas, janelas flutuantes e ações para encerrar apps. `AGPL-3.0`
* [essentials](https://github.com/sameerasw/essentials) ✨ - Ferramentas, mods e soluções alternativas essenciais para Pixels. Também compatível com outros dispositivos `MIT`
* [expressive-cutout](https://github.com/EvanKoe/expressive-cutout) - Dynamic Island offline seguindo o design Material Expressive, com notificações, blocos ao vivo e cores Material You `GPL-3.0`
* [Extendroid](https://github.com/legendsayantan/Extendroid) ✨ - Adiciona suporte a múltiplas janelas no estilo desktop em smartphones Android. `GPL-3.0`
* [FreeformShell](https://github.com/bravoyush/FreeformShell) - Auxiliar experimental de gerenciamento de janelas flutuantes que adiciona barras de título, bordas de redimensionamento e escala de tela por APIs do sistema via Shizuku. `Apache-2.0`
* [gama](https://github.com/palincat/gama) - Permite alternar entre os renderizadores OpenGL e Vulkan definindo a propriedade de sistema `MIT`
* [Google-Shortcuts-Launcher](https://github.com/WSTxda/Google-Shortcuts-Launcher) - Central de atalhos na gaveta de apps do launcher para recursos dos apps do Google; o Shizuku abre componentes do Google que de outra forma seriam inacessíveis. `GPL-3.0`
* [GSplit](https://github.com/Salat39/GSplit) ✨ - Predefinições de tela dividida e de múltiplas janelas flutuantes com agendamento, início automático no boot e overlays; um shell ADB opcional via Shizuku configura as divisões. `Proprietary`
* [HyperBridge](https://github.com/D4vidDf/HyperBridge) - Traz a experiência nativa do HyperIsland ao HyperOS levando as notificações para a interface ao redor do recorte da câmera, com temas e widgets `Apache-2.0`
* [Jarngreipr](https://github.com/BrianJr03/Jarngreipr) - Launcher para dispositivos de jogos com duas telas. Usa o Shizuku para mapear uma das telas sensíveis ao toque como entradas de controle `MIT`
* [Language-Selector](https://github.com/VegaBobo/Language-Selector) - Permite selecionar o idioma de cada app individualmente (Android 13+) `Apache-2.0`
* [Lightspeed](https://github.com/SBFlabs/Lightspeed) `IAP` 💰 - Estação de trabalho offline guiada por gestos e camada de controle sobre as interfaces das fabricantes, usando o Shizuku para navegação elevada e troca de apps fluida. `Proprietary`
* [LinkSheet](https://github.com/LinkSheet/LinkSheet) - Restaura o seletor de app para links (URL) do Android <12 com Material3 `Modified MPL-2.0`
* [Lockscreen Widgets](https://play.google.com/store/apps/details?id=tk.zwander.lockscreenwidgets) `IAP` 💰 - Exibe widgets na tela de bloqueio. O Shizuku só é necessário no Android 13 e posteriores `MIT` [(Código-fonte)](https://github.com/zacharee/LockscreenWidgets/)
* [LogCat Live Wallpaper](https://github.com/YasserNull/logcat-live-wallpaper) - Papel de parede animado que exibe a saída do Logcat na tela com cores, fontes e rolagem personalizáveis; usa Shizuku ou root para o log completo. `GPL-3.0`
* [MultiLocale](https://github.com/Nightdavisao/MultiLocale) - Um app simples que permite adicionar idiomas extras (ou "não suportados") às configurações de localidade do dispositivo, caso a fabricante (Xiaomi) não permita `MIT`
* [O.status](https://github.com/CATCHINGL/O.status) - Indicador minimalista na barra de status para Wi-Fi, rede celular e bateria que usa integração opcional com o Shizuku para combinar com as cores dos ícones do sistema. `Proprietary`
* [OmniPrompt](https://github.com/mrndstvndv/OmniPrompt) - Uma paleta de comandos Android focada no teclado que reúne busca de apps/dispositivo e utilitários do sistema em um overlay `GPL-3.0`
* [Renoir](https://github.com/exaclast/renoir) - Criador de temas Material You que aplica overlays personalizados por um comando shell do Shizuku. `Proprietary`
* [SetEditPlus](https://github.com/kerneldroid/SetEditPlus) ✨ - Editor das tabelas de configurações System/Secure/Global do Android com modos Shizuku/Root, rastreamento de alterações e persistência após o boot. `Proprietary`
* [sharemove](https://github.com/thejaustin/sharemove) - Oculta apps das telas de compartilhamento, "Abrir com" e seletor do instalador de APK do Android, suspendendo ou desativando componentes via Shizuku ou root. `GPL-3.0`
* [ShizukuShortcuts](https://github.com/yshalsager/ShizukuShortcuts) - Crie atalhos no launcher para comandos shell `GPL-3.0`
* [ShizuTools](https://github.com/legendsayantan/ShizuTools) ✨ - Reúne algumas ferramentas fáceis de usar para ir além do nível de controle permitido pelo sistema Android `GPL-3.0`
* [Smart Dock](https://f-droid.org/packages/cu.axel.smartdock/) - Transforme seu celular em um ambiente desktop com barra de tarefas, apps recentes e menu iniciar `GPL-3.0` [(Código-fonte)](https://github.com/axel358/smartdock)
* [Smart Edge](https://f-droid.org/en/packages/com.imi.smartedge.sidebar.panel/) - Um painel lateral para Android altamente personalizável inspirado no OriginOS `MIT` [(Código-fonte)](https://github.com/Imtiaz-Official/Smart-Edge)
* [Smart Island](https://github.com/agupta07505/SmartIsland) - Um overlay leve para Android que transforma notificações, chamadas e reprodução de mídia em uma ilha flutuante de consulta rápida `GPL-3.0`
* [SmartspacerPlugins](https://github.com/KieronQuinn/SmartspacerPlugins) - Plugins para o Smartspacer `GPL-3.0`
* [SuperShade](https://github.com/thejaustin/SuperShade) - Substituto da aba de notificações que controla brilho, expansão da barra de status e ações de energia por comandos shell do Shizuku. `Proprietary`
* [SysReadout-Launcher](https://github.com/AndSni/SysReadout-Launcher) - Launcher em estilo terminal que transforma a tela inicial em um monitor do sistema ao vivo, com linhas de status fixadas, tabelas de processos/conexões/DNS e um log de eventos, lendo dados do sistema pelo Shizuku. `GPL-3.0`
* [System UI Tuner](https://github.com/zacharee/Tweaker) - Visualize e modifique configurações ocultas em dispositivos Android `MIT`
* [TapTap](https://github.com/KieronQuinn/TapTap) ✨ - Port do recurso de toque duplo na traseira do dispositivo do Android 12 para qualquer dispositivo com Android 7.0+ `GPL-3.0`
* [Tarnhelm](https://f-droid.org/packages/cn.ac.lz233.tarnhelm/) ✨ - Remove rastreamento de links compartilhados. Suporta regras personalizadas de reescrita de URL `GPL-3.0` [(Código-fonte)](https://github.com/lz233/Tarnhelm)
* [Taskbar](https://f-droid.org/packages/com.farmerbb.taskbar/) - Use um menu iniciar para acessar apps. O Shizuku pode desbloquear recursos adicionais `Apache-2.0` [(Código-fonte)](https://github.com/farmerbb/Taskbar)
* [WidgetsPro](https://github.com/preethamkmr3/WidgetsPro) - Widgets de CPU e bateria `Proprietary`
* [YoukiDEX](https://github.com/mrYouki/YoukiDex-Android-Desktop) - Uma camada completa de experiência desktop para Android `GPL-3.0`

### Development utilities

* [80bee-app](https://github.com/Endda/80bee-app) - Caixa de ferramentas ADB/Fastboot no próprio aparelho, sem root: modos de boot, DPI, DNS, debloater e contorno de sideload via Shizuku, além do modo host USB-OTG. `Apache-2.0`
* [ActivityLauncherShizukuPlugin](https://github.com/ActivityLauncher/ActivityLauncherShizukuPlugin) - Plugin baseado em Shizuku para o [Activity Launcher](https://github.com/ActivityLauncher/ActivityLauncher) que permite abrir activities privadas (não exportadas). `GPL-3.0`
* [ActivityManager](https://github.com/sdex/ActivityManager) ✨ - Abre activities ocultas e não exportadas diretamente, sem root `Apache-2.0`
* [ADB Captain](https://github.com/eatenlamp/adbcaptain) - Kit de ferramentas ADB que executa comandos de shell, gerenciamento de apps e acesso a logs pelo Shizuku, sem precisar de root. `AGPL-3.0`
* [Android Code Studio](https://github.com/AndroidCSOfficial/android-code-studio) - IDE no próprio aparelho para compilar projetos Android baseados em Gradle; o Shizuku permite a instalação silenciosa do APK gerado. `GPL-3.0`
* [AndroidAccounts](https://github.com/iamr0s/AndroidAccounts) - Lista os nomes de pacote dos apps que registraram uma conta para um usuário. `Proprietary`
* [Cosmic-IDE](https://github.com/Cosmic-Ide/Cosmic-IDE) - IDE para desenvolvimento JVM. Usa o Shizuku para um shell embutido `GPL-3.0`
* [debuggable-app-data-backup](https://github.com/timschneeb/debuggable-app-data-backup) - Faz backup/restauração dos dados privados de apps depuráveis usando o Shizuku `GPL-3.0`
* [DEVTools](https://github.com/MetxStudio/DEVTools) - Kit completo de desenvolvimento Android: terminais, monitor de sensores, gerenciadores de apps/arquivos e um auxiliar de shell via Shizuku. `MIT`
* [DroidPerf](https://github.com/fortifying/DroidPerf) - Overlay de FPS e telemetria de hardware em tempo real que mede a entrega real de quadros pelo SurfaceFlinger; o Shizuku é necessário para FPS alvo, tempos de quadro e detecção de apps em nível de shell. `Proprietary`
* [DSU-Sideloader](https://github.com/VegaBobo/DSU-Sideloader) - App simples feito para ajudar a instalar GSIs facilmente pelo recurso DSU do Android. `Apache-2.0`
* [dualapp-mediastore-compatibility](https://github.com/kaedea/dualapp-mediastore-compatibility) - Corrige problemas de compatibilidade de MediaStore e E/S de arquivos entre o app do HostProfile e WorkProfile/DualApp/MultiApp. `Proprietary`
* [FPS-Meter-Android](https://github.com/rdevz-ph/FPS-Meter-Android) - Overlay leve e de alto desempenho para monitorar FPS, inspirado no Samsung Perf Z, para jogos e testes de desempenho `MIT`
* [FPSViewer](https://github.com/binhmod/FPSViewer) - Overlay de visualização de FPS com gráfico `Proprietary`
* [FrameX-Android](https://github.com/MaheshSharan/FrameX-Android) - Overlay de desempenho em tempo real para Android `MIT`
* [get_event](https://github.com/lalakii/get_event) - Lê /dev/input/event* `Proprietary`
* [IntentX](https://github.com/wxxsfxyzm/IntentX) - Explora apps e activities instalados e cria, testa e dispara intents com acesso normal, root ou Shizuku; salva intents como atalhos. `GPL-3.0`
* [LibChecker](https://github.com/LibChecker/LibChecker) - App para ver as bibliotecas usadas pelos apps do seu aparelho. Usa o Shizuku para identificar a origem de instalação de outros apps. `Apache-2.0`
* [LogFox](https://github.com/F0x1d/LogFox) ✨ - Mais um leitor de logcat para Android `GPL-3.0`
* [LogSleuth](https://github.com/shiaho777/LogSleuth) - Visualizador de logcat poderoso e sem root, com SDK de logging embutível, transmissão ao vivo, busca, filtros, detecção de crash/ANR e replay de sessão. `Apache-2.0`
* [ManageSensors](https://github.com/Carry-rrk/ManageSensors) - Usa o Shizuku para chamar as APIs de AppOps e controlar com precisão as permissões dos apps `MIT`
* [panda-ide](https://github.com/ferelking242/panda-ide) - IDE Flutter pensada para celular, com editor de código, terminal PTY, Git e extensões do VS Code; uma ponte Shizuku fornece shell em nível de ADB para rodar flutter run no próprio aparelho. `MIT`
* [roamer](https://github.com/eigenlux-ai/roamer) - Ferramenta de desenvolvimento que substitui o ISO de país do SIM e o nome da operadora via Shizuku, com sincronização opcional de idioma por app. `MIT`
* [RootActivityLauncher](https://play.google.com/store/apps/details?id=tk.zwander.rootactivitylauncher) `Paid` 💰 - Abre e interage com activities, services e receivers (não) exportados. Suporta Shizuku além de root. `GPL-3.0` [(Código-fonte)](https://github.com/zacharee/RootActivityLauncher)
* [wireless-adb-switch](https://github.com/Smooth-E/wireless-adb-switch) - Widgets e bloco de configurações rápidas para ligar/desligar a depuração sem fio (com integração ao KDE Connect) `GPL-3.0`

### Device owner (DPM)

* [Déchaîner](https://github.com/warleysr/dechainer) - Bloqueia conteúdo adulto como Device Owner; o Shizuku executa o comando de configuração dpm set-device-owner. `Apache-2.0`
* [Dhizuku](https://github.com/iamr0s/Dhizuku) - App inspirado no Shizuku que permite compartilhar permissões de DeviceOwner com apps de terceiros `GPL-3.0`
* [harbor](https://f-droid.org/packages/com.monstera.harbor/) - Gerenciador de perfil de trabalho com ferramentas Shizuku opcionais para automação `Apache-2.0` [(Código-fonte)](https://github.com/Stem0794/harbor)
* [OwnDroid](https://github.com/BinTianqi/OwnDroid) ✨ - Gerencie seu aparelho com privilégios de Device owner `GPL-3.0`
  * [MDPC](https://github.com/MrRare2/MDPC) - Fork do OwnDroid com recursos adicionais `GPL-3.0`

### Display management
* [Adaptive-Hz](https://github.com/mahmutaunal/Adaptive-Hz) - Alterna automaticamente a taxa de atualização da tela entre 60Hz e 120Hz conforme a interação do usuário. Feito para aparelhos Samsung sem taxa adaptativa real `MIT`
* [akiHz](https://github.com/anlaki-py/akihz) - Alternador leve de taxa de atualização com bloco nas Configurações rápidas, detecção automática de taxa e monitor de FPS flutuante `MIT`
* [android-display-extend](https://github.com/jqssun/android-display-extend) ✨ - Gerenciador de telas físicas e virtuais com touchscreen virtual embutido. Ótimo para usar com `scrcpy --new-display` num PC `GPL-3.0`
* [android-display-mirror](https://github.com/jqssun/android-display-mirror) ✨ - Central de espelhamento de tela com suporte a compartilhar o conteúdo da tela via AirPlay, Moonlight/Sunshine e DisplayLink `GPL-3.0`
* [BetterNightLight](https://github.com/paulsnuff/BetterNightLight) - Dá controle avançado sobre a Luz noturna nativa do Android: agendamento, fases de reforço e temperatura de cor precisa, via acesso a configurações seguras com Shizuku ou root. `GPL-3.0`
* [deskcontrol](https://github.com/exiarepairii/deskcontrol) - Transforma o celular em touchpad e teclado para um único app rodando numa tela externa conectada por cabo `GPL-3.0`
* [Dextop](https://github.com/NarYuki/Dextop) ✨ - Ambiente de desktop usando Samsung DeX ou Shizuku, com multitarefa e resolução personalizada `GPL-3.0`
* [Fold_Switcher](https://github.com/eiyooooo/Fold_Switcher) - Alterna entre os vários estados de dobra da tela em aparelhos dobráveis `Apache-2.0`
* [GrayPause](https://f-droid.org/packages/com.lpw.graypause/) - Keeps your phone in grayscale and runs self-ending color breaks on a timer, with a Quick Settings tile, launcher shortcuts, countdown notifications and per-app color exceptions `GPL-3.0` [(Código-fonte)](https://metaheavens.de/forgejo/metaheavens/graypause)
* [Grayscaler](https://github.com/C10udburst/Grayscaler) - Mantém o celular quase todo em preto e branco, mas permite que apps como a câmera fiquem coloridos `GPL-3.0`
* [magicdesk](https://github.com/mekhontsev/magicdesk) - Estação de trabalho de código aberto para Android 15+, com janelas nativas, telas externas, áreas de trabalho e integração com o Termux via Shizuku `GPL-3.0`
* [PortalPad](https://github.com/Smart-Home-User/PortalPad) - Transforma o celular em trackpad, air mouse e controle remoto para telas externas, como óculos de RA, monitores e TVs `MIT`
* [SecondScreen](https://play.google.com/store/apps/details?id=com.farmerbb.secondscreen.free) - Espelhamento de tela melhor para aparelhos Android `Apache-2.0` [(Código-fonte)](https://github.com/farmerbb/SecondScreen)
* [Tideo Auto Brightness](https://github.com/faded-penguin021/Tideo-Auto-Brightness) - Substituto transparente do brilho adaptável, com decisões explicáveis e suporte a ritmo circadiano. `MIT`

### Entertainment

* [Aniyomi](https://github.com/aniyomiorg/aniyomi) - Fork do Tachiyomi com suporte a anime e gerenciamento de plugins usando o Shizuku. `Apache-2.0`
* [BiliDownOut](https://f-droid.org/packages/cn.a10miaomiao.bilidown/) - Exporta vídeos baixados pela versão Android do Bilibili `GPL-3.0` [(Código-fonte)](https://github.com/10miaomiao/bili-down-out)
* [Crosstune](https://github.com/astrovm/crosstune) - Opens any music link in your preferred app with exact match, playlists and synced lyrics; one-tap setup via Shizuku `MIT`
* [hlbmerge_flutter](https://github.com/molihuan/hlbmerge_flutter) - Junta e exporta arquivos de cache do BiliBili em MP4, com suporte a cliente móvel e de computador `Apache-2.0`
* [Mihon](https://github.com/mihonapp/mihon) - Leitor de mangá com gerenciamento de plugins via Shizuku. Sucessor independente do Tachiyomi. `Apache-2.0`
  * O Mihon/Tachiyomi tem vários outros forks ativos, incluindo [TachiyomiSY](https://github.com/jobobby04/TachiyomiSY) e [TachiyomiAZ](https://github.com/az4521/TachiyomiAZ)

### File management
* [Buge-Files](https://bugestudio.website/files/) - Gerenciador de arquivos Material 3 Expressive que instala APKs pelo Shizuku, além de navegar e gerenciar o armazenamento. `GPL-3.0` [(Código-fonte)](https://github.com/BugeStudioTeam/Buge-Files)
* [Butler](https://github.com/d4rken-org/butler) `IAP` 💰 - Explorador de arquivos rápido e privado para usuários avançados, com abas, lixeira, busca por regex, gerenciador de apps e suporte a root/Shizuku `GPL-3.0`
* [Continuum Explorer (Memories)](https://github.com/johakovi/Continuum-Explorer-Memories) - Gerenciador de arquivos multimídia de nível desktop para DeX, tablets e celulares, com visualizadores de mídia/PDF, arquivos compactados, armazenamento em rede e saves de jogos, usando o Shizuku para acesso privilegiado a arquivos. `GPL-3.0`
* [FileExplorer](https://github.com/SysAdminDoc/FileExplorer) - Gerenciador de arquivos para armazenamento local, root, arquivos compactados, compartilhamentos de rede, nuvem, cofres e análise de armazenamento `MIT`
* [fluffy](https://apt.izzysoft.de/fdroid/index/apk/app.fluffy) - Gerenciador de arquivos e visualizador de arquivos compactados com suporte a Android TV. Permite acesso total aos arquivos usando o Shizuku, se ativado nas configurações `GPL-3.0` [(Código-fonte)](https://github.com/mlm-games/fluffy)
* [Hexora](https://github.com/ZENINXOP/Hexora) - Dual-pane file manager fork of MP-Manager with archive browsing, built-in editor and APK tools, with Shizuku support for elevated access `GPL-3.0`
* [immich-cloud-media](https://github.com/Dreaming-Codes/immich-cloud-media) - Provedor de mídia em nuvem que exibe uma biblioteca Immich auto-hospedada no seletor de fotos do sistema Android, configurado via Shizuku ou ADB. `GPL-3.0`
* [KArchiver](https://github.com/sysrv64/KArchiver) - Gerenciador de arquivos Android centrado em arquivos compactados: navega no armazenamento, abre e edita ZIP/TAR/7Z no lugar, busca dentro de arquivos e arquivos compactados, com motor opcional Shizuku ou root para caminhos restritos `GPL-3.0`
* [MaterialFiles](https://github.com/zhanghai/MaterialFiles) ✨ - Gerenciador de arquivos em Material Design para Android `GPL-3.0`
* [MP-Manager](https://github.com/AbdurazaaqMohammed/MP-Manager) ✨ - Gerenciador de arquivos Material de dois painéis focado em APKs, alternativa de código aberto ao MT Manager, com gerenciamento privilegiado de arquivos via root e Shizuku. `GPL-3.0`
* [NFile](https://github.com/Senzme/NFile) - Gerenciador de arquivos com acesso às pastas do Android usando o Shizuku `GPL-3.0`
* [plain-app](https://github.com/plainhub/plain-app) - Painel web auto-hospedado para gerenciar arquivos, mídia, contatos, SMS e chamadas pelo navegador, com Shizuku para exclusão privilegiada de SMS. `AGPL-3.0`
* [RippleFiles](https://github.com/GokulSB/RippleFiles-FileManager) - Gerenciador de arquivos Material expressivo com armazenamento local e em nuvem, além de acesso a Android/data liberado pelo Shizuku. `MIT`
* [ROSE](https://github.com/NarayanChetri/ROSE) - Gerenciador de arquivos moderno com interface Material 3, suporte a arquivos compactados, lixeira e acesso a Android/data e Android/obb via Shizuku, sem root. `GPL-3.0`
* [SDMaid-SE](https://play.google.com/store/apps/details?id=eu.darken.sdmse) ✨ `IAP` 💰 - O SD Maid 2/SE é a ferramenta de limpeza mais completa do Android `GPL-3.0` [(Código-fonte)](https://github.com/d4rken-org/sdmaid-se)
* [sync-to-android-data](https://github.com/kamren-zirger/sync-to-android-data) - Sincroniza arquivos para dentro e para fora das pastas restritas Android/data quando os apps alvo abrem ou fecham `MIT`
* [twig](https://github.com/dev2ex/twig) - Gerenciador de arquivos de dois painéis focado em tamanho reduzido (~7MB) para armazenamento local, arquivos compactados, FTP/SFTP/SMB/WebDAV/S3/restic/Jellyfin `GPL-3.0`
* [UnscopeMyData](https://github.com/kepatotorica/UnscopeMyData) - Move dados de apps para dentro e para fora das pastas de armazenamento com escopo, usando o Shizuku para acesso elevado a arquivos. `GPL-3.0`
* [XArchiver](https://github.com/Xtra-Manager-Software/XArchiver) - Gerenciador de arquivos com suporte embutido a arquivos compactados `MIT`
* [XClean](https://github.com/utopiafar/XClean) - Limpador baseado em regras, com motores Normal, Shizuku e Root, para remover lixo de apps. `Proprietary`
* [XFiles](https://github.com/Local1stDotApp/XFiles) - Gerenciador de arquivos offline com suporte a root e Shizuku para acesso total ao sistema de arquivos `GPL-3.0`
* [ZenFile](https://github.com/l930203811/ZenFile) - Fork do NFile com suporte embutido a servidor remoto de arquivos `GPL-3.0`
* [ZhuFiler](https://github.com/Artzhu86/ZhuFiler) - Gerenciador de arquivos Material You de código aberto, com arquivos compactados, editor, reprodução de mídia, manipulação de APKs e acesso privilegiado via Shizuku. `MIT`

> [!NOTE]
> [Veja aqui mais gerenciadores de arquivos (código fechado)](pages/CLOSED_SOURCE_pt-BR.md#file-management)

### Games

* [ADOFAI-Key-Viewer-Mobile](https://github.com/QuyetGD-15/ADOFAI-Key-Viewer-Mobile) - Visualizador de teclas em overlay para ADOFAI e jogos de ritmo; lê eventos de entrada do hardware pelo getevent via Shizuku para visualização de toques com latência ultrabaixa, medição de KPS e contagem de cliques. `Proprietary`
* [AimBuddy](https://github.com/1337Xcode/AimBuddy) - Assistente de mira no próprio aparelho para jogos Android: captura de tela em tempo real, detecção de objetos e overlays de rastreamento de alvo; entrada assistida opcional pelo injectInputEvent via Shizuku. `Proprietary`
* [Ascent](https://github.com/4o3F/Ascent) - Ferramenta para obter os links do histórico de gacha dos jogos da Mihoyo  `AGPL-3.0`
* [BDroid_X](https://github.com/Ark-Repoleved/BDroid_X) - Gerenciador de mods do Browndust II `MIT`
* [Cinderbox-Companion](https://github.com/ObfuscatedVoid/Cinderbox-Companion) - App complementar para Stardew Valley no Android, com sincronização de saves pelo Steam Cloud, download dos arquivos do jogo e gerenciamento de mods SMAPI `MIT`
* [CloudSync-Mobile](https://github.com/StardewValleyMods/CloudSync-Mobile) - App que permite sincronizar seus saves de Stardew Valley entre vários aparelhos `GPL-3.0`
* [lac-tool](https://github.com/aliernfrog/lac-tool) - Gerencia mapas, papéis de parede e capturas de tela do jogo 'Los Angeles Crimes' `GPL-3.0`
* [linkura-localify](https://github.com/ChocoLZS/linkura-localify) - Plugin de localização para Link! Like! LoveLive! que traduz os textos do jogo via LLM `GPL-3.0`
* [LOModInstaller](https://github.com/anyabot/LOModInstaller) - Gerenciador de mods do jogo 'Last Origin' `Proprietary`
* [MAA-Meow](https://github.com/Aliothmoon/MAA-Meow/blob/main/README_EN.md) - Roda o MAA nativamente no Android para fazer as tarefas diárias do Arknights com um toque, em modo primeiro plano ou segundo plano `AGPL-3.0`
* [mt-en-applier](https://github.com/Aikiooo/mt-en-applier) - Instalador com um toque do patch não oficial em inglês do jogo mobile Mushoku Tensei, copiando os arquivos via Shizuku sem root nem PC. `Proprietary`
* [Nibnya](https://github.com/yinghuajimew/Nibnya) - Editor NBT para Android do Minecraft Bedrock, com Shizuku para acesso a /data `AGPL-3.0`
* [Okkei Patcher](https://github.com/solrudev/OkkeiPatcher) - App complementar para localizar a versão Android da visual novel CHAOS;CHILD `GPL-3.0`
* [pf-tool](https://github.com/aliernfrog/pf-tool) - Importe e compartilhe mapas do Polyfield com facilidade `GPL-3.0`
* [pogoplusle](https://github.com/Mygod/pogoplusle) - Pula a caixa de pareamento ao conectar um Pokémon GO Plus `Apache-2.0`
* [ShinGen](https://github.com/Shio2077/ShinGen#genshin-impact-auto-conversation-clicker-on-android) - Clicador automático de diálogos do Genshin Impact `MIT`
* [stalker](https://github.com/onerdna/stalker) - Visualizador e editor de saves do Shadow Fight 2 `GPL-3.0`
* [SwiftSense](https://github.com/itsmelissadev/SwiftSense) - Otimizador para jogos que usa o Shizuku para congelar apps em segundo plano, desativar pacotes e aumentar a taxa de amostragem dos sensores. `GPL-3.0`
* [translatefgo](https://github.com/rayshift/translatefgo) - Projeto de tradução do jogo Fate/Grand Order `MIT`

### Input methods

* [8bitdo-xbox-bridge](https://github.com/BoredNewCoder/8bitdo-xbox-bridge) - Faz o 8BitDo Ultimate Wired Controller for Xbox funcionar como um gamepad de verdade em todo o sistema no Android TV, via protocolo GIP obtido por engenharia reversa e injeção uinput pelo Shizuku. `MIT`
* [BiBi Keyboard](https://github.com/BryceWG/BiBi-Keyboard/blob/main/README_EN.md) - Teclado de entrada por voz com IA; o Shizuku ou root mantém ativo o serviço em segundo plano da bola flutuante e das teclas de volume. `Apache-2.0`
* [ButtonSilencer](https://github.com/EithonX/ButtonSilencer) - Bloqueia botões defeituosos de fones de ouvido e controles de IEM sem desativar os botões do próprio celular; o Shizuku fornece o caminho privilegiado para proteger a entrada do fone com a tela desligada. `MIT`
* [C9](https://github.com/austinauyeung/C9) - Cursor eficiente baseado em grade, oferecido junto com um cursor tradicional. O Shizuku só é necessário no Android 11. `Apache-2.0`
* [GameShift](https://github.com/tientien17/GameShift) - Troca automaticamente o launcher padrão quando um controle de jogo é conectado e o restaura ao desconectar, usando o Shizuku sem root. `Apache-2.0`
* [Joycon2Android](https://github.com/JoeGeC/joycon2android) - Conecta os controles Joy-Con do Nintendo Switch 2 por BLE e os expõe como gamepads virtuais em todo o sistema via um relay UHID pelo Shizuku. `GPL-3.0`
* [KeyMapper](https://play.google.com/store/apps/details?id=io.github.sds100.keymapper) ✨ - Um app Android que muda o que os botões fazem nos seus aparelhos! `GPL-3.0` [(Código-fonte)](https://github.com/keymapperorg/KeyMapper)
* [keysync](https://github.com/aka-munan/keysync) - Jogue com mouse e teclado no aparelho Android; mapeador de teclas para jogos `Apache-2.0`
* [OpenMapper](https://github.com/kinou-p/android-open-mapper) - Mapeador de gamepad gratuito e de código aberto que usa o Shizuku para injetar toques com latência abaixo de um milissegundo; alternativa ao Mantis e ao Panda. `PolyForm-Noncommercial-1.0.0`
* [pastiera](https://github.com/palsoftware/pastiera) - Teclado Android especializado em aparelhos com teclado físico. Usa o Shizuku para gestos no trackpad `GPL-3.0`
* [Steam Controller for Android](https://github.com/SonicDX12/SteamController-Android) - Usa o Steam Controller 2026 como um gamepad Android de verdade via uinput do Linux pelo Shizuku; USB, dongle ou BLE. `MIT`
* [TitanPad](https://github.com/sztupy/TitanPad) - Converte a entrada capacitiva do teclado físico do Titan2 em gestos de mouse e rolagem. Usa o Shizuku para ler a entrada do trackpad e configurar dispositivos HID virtuais `Apache-2.0`
* [XtMapper](https://github.com/Xtr126/XtMapper) - Mapeador de teclas para Android x86 `GPL-3.0`


### Installer & app stores

* [APKUpdater](https://github.com/DmitryN71/apkupdater) - Fork do APKUpdater que adiciona instalações silenciosas via Shizuku às fontes APKMirror, Aptoide, F-Droid e IzzyOnDroid. `GPL-3.0`
* [AuroraDroid](https://f-droid.org/packages/com.aurora.adroid/) - Cliente F-Droid livre com instalações silenciosas via Shizuku/root e atualizações automáticas `GPL-3.0` [(Código-fonte)](https://gitlab.com/AuroraOSS/auroradroid)
* [AuroraStore](https://f-droid.org/packages/com.aurora.store/) - Alternativa de código aberto à Google Play Store, com privacidade e design moderno `GPL-3.0` [(Código-fonte)](https://gitlab.com/AuroraOSS/AuroraStore)
* [BHub](https://github.com/B1ays/BHub) - Baixe, instale e compartilhe mods com facilidade `Proprietary`
* [Discoverium](https://github.com/cygnusx-1-org/Discoverium) - Fork do Obtainium para descobrir e instalar apps direto da fonte, com backends de instalação Shizuku, Dhizuku e Sui. `GPL-3.0`
* [Droid-ify](https://f-droid.org/packages/com.looker.droidify/) - Cliente F-Droid em Material `GPL-3.0` [(Código-fonte)](https://github.com/Droid-ify/client)
* [ffupdater](https://f-droid.org/packages/de.marmaro.krt.ffupdater/) - FFUpdater: atualizador de navegadores focados em privacidade `GPL-3.0` [(Código-fonte)](https://github.com/Tobi823/ffupdater)
* [florid](https://github.com/Nandanrmenon/florid) - Cliente F‑Droid em Material3 `GPL-3.0`
* [GitHub-Store](https://f-droid.org/packages/zed.rainxch.githubstore/) - Loja de apps para releases do GitHub, com função de descoberta `Apache-2.0` [(Código-fonte)](https://github.com/komi-store/komi-store)
* [instafel](https://github.com/mamiiblt/instafel) - App atualizador do Instafel, um mod do Instagram `MIT`
* [InstallerX-Revived](https://github.com/wxxsfxyzm/InstallerX-Revived) ✨ - Substituto moderno e funcional do instalador de apps do Android `GPL-3.0`
* [InstallWithOptions](https://github.com/zacharee/InstallWithOptions) ✨ - App relativamente simples que usa o Shizuku para instalar APKs no aparelho com opções avançadas `MIT`
* [IzzyOnDroid](https://gitlab.com/sunilpaulmathew/izzyondroid) - Cliente não oficial do repositório F-Droid IzzyOnDroid `GPL-3.0`
* [KingInstaller](https://github.com/fcaronte/KingInstaller) - Instalador de APK que falsifica a identidade de instalador da Play Store para contornar restrições de visibilidade de apps, instalando via intents, Shizuku ou root `GPL-3.0`
* [LocalAndroidStore](https://github.com/SysAdminDoc/LocalAndroidStore) - Catálogo privado de apps que instala releases assinados do GitHub e do F-Droid, opcionalmente por uma sessão de instalação do Shizuku. `MIT`
* [multistore](https://github.com/FedeFluork/multistore) - Reúne lojas de apps de terceiros num único catálogo para buscar, comparar, baixar e atualizar APKs `GPL-3.0`
* [Neo-Store](https://f-droid.org/packages/com.machiav3lli.fdroid/) - Cliente F-Droid com interface moderna e um arsenal de recursos extras `GPL-3.0` [(Código-fonte)](https://github.com/NeoApplications/Neo-Store)
* [Obtainium](https://github.com/ImranR98/Obtainium) - Receba atualizações de apps Android direto da fonte `GPL-3.0`
  * [ObtainX](https://f-droid.org/packages/dev.bikram.obtainx/) - Fork do Obtainium com interface redesenhada em Material 3 `GPL-3.0` [(Código-fonte)](https://github.com/bikram-agarwal/ObtainX)
* [Omnify](https://github.com/Victor-root/Omnify) - Fork de cliente F-Droid que também instala apps de fontes externas, com instalador via Shizuku e uma linha de descoberta "Funciona com Shizuku". `GPL-3.0`
* [OpenLoader](https://github.com/thebytearray/OpenLoader) - Instalador de APK feito para a era da verificação de desenvolvedores do Android, usando o Shizuku para o caminho de instalação privilegiado. `GPL-3.0`
* [Orion Store](https://github.com/RookieEnough/Orion-Store) - Loja de apps modificados `GPL-3.0`
* [PI](https://github.com/SanmerApps/PI) - Instalador de pacotes que permite sobrescrever o solicitante e o executor do pacote `MIT`
* [SAI](https://f-droid.org/packages/com.aefyr.sai.fdroid/) - Instalador de APKs divididos (split APKs) para Android `GPL-3.0` [(Código-fonte)](https://github.com/Aefyr/SAI)
* [ShizuCoreFetch](https://github.com/elhizazi1/ShizuCoreFetch) - Gerenciador de apps com Shizuku, com instalações silenciosas, atualizações e operações em lote `GPL-3.0`
* [Shizuku Package Installer](https://github.com/vvb2060/PackageInstaller) - Substituto leve do instalador de apps com suporte a split APK `Apache-2.0`
* [ShizuStore](https://github.com/timschneeb/ShizuStore) ✨ - Loja de apps para apps Shizuku. Baseada nesta lista awesome-shizuku, instala APKs direto das fontes originais `GPL-3.0`
* [tern](https://github.com/munzzyy/tern) - Atualizador no estilo do Obtainium que verifica nome do pacote, certificado de assinatura e checksums do publicador antes de instalar via Shizuku, Dhizuku, root ou o instalador do sistema, em celulares, tablets e TV. `GPL-3.0`
* [universal-installer](https://github.com/pass-with-high-score/universal-installer) - Instala e gerencia pacotes APK com suporte a split APK, instalação silenciosa via Shizuku e verificação de malware pelo VirusTotal `GPL-3.0`
* [Vyxel Apps](https://github.com/NikhilKain/vyxel-apps) `IAP` 💰 - Loja de apps baseada no GitHub, com verificação de assinatura e instalações silenciosas pelo Shizuku. `AGPL-3.0`
* [yuki](https://github.com/carlelieser/yuki) - Catálogo e vitrine de apps Shizuku de código aberto, coletados do GitHub `MIT`

### Miscellaneous

* [AppBooster](https://github.com/androidexpert35/AppBooster) - Interface gráfica para o utilitário embutido `dex2oat` do Android, que permite reotimizar o código DEX dos apps instalados `Apache-2.0`
* [CaptureCap](https://github.com/yepgoryo/CaptureCap) - App de gravação e transmissão de tela e áudio, sem precisar de root `MIT`
* [Device Watch](https://github.com/jrs8205/Device-Watch) - Monitor offline do aparelho com widgets, análise de uso por app e protetor de tela durante o carregamento; o acesso opcional via Shizuku revela estatísticas de bateria, carga real de CPU/GPU e temperaturas. `GPL-3.0`
* [Fern](https://github.com/wized2/Fern) - Monitor de sistema ao vivo em Material 3 para CPU, RAM, armazenamento, bateria, temperatura e rede; modo Avançado com Shizuku/root para CPU/RAM reais por app, temperaturas e forçar parada. `MIT`
* [ghostlock-app](https://github.com/YuKongA/ghostlock-app) - App de escalonamento de privilégios com um toque (CVE-2026-43499) que concede uid 0 temporário em muitos aparelhos de fábrica; os perfis de kernel que exigem Shizuku rodam por um shell Shizuku. `Apache-2.0`
* [HiddenAlarmRevealer](https://github.com/AhmetCanArslan/HiddenAlarmRevealer) - Descobre por que o ícone de alarme está ativo na barra de status `Proprietary`
* [IrisShot](https://github.com/raging-flames/IrisShot) - Ferramenta de captura de tela com rolagem para jogos Android, que rola automaticamente e junta capturas longas usando MediaProjection ou captura por shell via Shizuku. `Proprietary`
* [KeiOS](https://github.com/hosizoraru/KeiOS) - Console de utilitários do sistema com servidor MCP local, acompanhamento de releases do GitHub, instalações privilegiadas via Shizuku ou root e ferramentas auxiliares para Blue Archive `Apache-2.0`
* [kiosk-satellite](https://github.com/jxlarrea/kiosk-satellite) - Quiosque do Home Assistant: satélite de voz, música sincronizada e protetor de tela com fotos, usando o Shizuku para atualizações privilegiadas de APK e ponte com o aparelho. `Proprietary`
* [krude](https://github.com/KusStar/krude) - Launcher completo de apps e fluxos de trabalho `MIT`
* [Mafza](https://github.com/yshalsager/Mafza) - Executor de ações de emergência com um perfil configurável, gatilhos de emergência externos e um modo seguro de simulação (Dry Run) `Proprietary`
* [NekokoLPA2](https://github.com/iebb/NekokoLPA2) - Gerenciador multiplataforma de eSIM/eUICC; no Android, pede ao Shizuku para abrir o socket QRTR exclusivo do shell para operações de perfil Telephony/TMAPI `MIT`
* [NotiFixer](https://github.com/dkajan19/NotiFixer) - Utilitário Android para tornar notificações persistentes/impossíveis de dispensar usando o Shizuku `MIT`
* [OnStop2FinishAndRemoveTask](https://github.com/takusan23/OnStop2FinishAndRemoveTask) - Fecha automaticamente os apps selecionados quando você sai deles, para economizar energia e memória `Apache-2.0`
* [overlay-translator](https://github.com/ciddwd/overlay-translator) ✨ - Tradutor de tela em tempo real para jogos, visual novels e mangás, com OCR no aparelho/na nuvem e overlay flutuante `Apache-2.0`
* [PhoneDiagnosticTool](https://github.com/ScoobyDouche/PhoneDiagnosticTool) - Diagnóstico do celular no próprio aparelho para CPU, GPU, bateria, RAM, armazenamento, sensores e tela, com leituras elevadas opcionais via Shizuku/root. `MIT`
* [PoC-Deployer-System](https://github.com/wqry085/PoC-Deployer-System) - Explora a CVE-2024-31317 para injeção no Zygote, integrando terminal remoto e transferência de arquivos `MIT`
* [Rainy Screenshot](https://github.com/CATMIAOZHI/RainyScreenShot/blob/main/README_EN.md) - Capturas e gravação de tela silenciosas por um shell privilegiado Shizuku ou Porter, em vez de MediaProjection. `Proprietary`
* [Screen Recorder](https://github.com/muhammadhaseebiqbal-dev/Screen-Recorder) - Gravador de tela com captura do áudio interno roteada pelo Shizuku. `MIT`
* [silent-alarm](https://github.com/izumisagirii/silent-alarm) - Despertador pensado para fones de ouvido que mantém os alarmes funcionando em ROMs agressivas de fabricantes, com um watchdog via Shizuku ou root que reinicia o app. `AGPL-3.0`
* [SimpleWear](https://play.google.com/store/apps/details?id=com.thewizrd.simplewear) - App simples para controlar seus aparelhos Android pelo relógio WearOS `Apache-2.0` [(Código-fonte)](https://github.com/SimpleAppProjects/SimpleWear)
* [telegram-rc](https://github.com/telegram-sms/telegram-rc) - Controle seu aparelho remotamente por mensagens do Telegram `BSD 3-Clause`
* [VineOS](https://github.com/Hexadecinull/VineOS) - Motor de VM Android; o Shizuku testa os privilégios de shell para o caminho sem root via ADB e depuração sem fio. `GPL-3.0`

### Network

* [ADNS](https://github.com/eyalm2000/adns) - Bloqueador de anúncios baseado em DNS para Android `MIT`
* [Bluetooth Bouncer](https://github.com/harvzor/android-bluetooth-bouncer) - Controle de conexão automática Bluetooth por dispositivo, que mantém o pareamento; a política é aplicada via Shizuku. `GPL-3.0`
* [bunnylock](https://github.com/btsearch/bunnylock) - Lock 2G/3G/4G/5G bands, RATs, frequencies and cells without root, picking the best backend available (Qualcomm, MediaTek, Pixel Tensor, Exynos, radio HAL) `GPL-3.0`
* [CellReader](https://play.google.com/store/apps/details?id=dev.zwander.cellreader) `Paid` 💰 - Lê informações de torres de celular no Android `MIT` [(Código-fonte)](https://github.com/zacharee/CellReader)
* [de1984](https://github.com/dorumrr/de1984) - Firewall de apps sem usar VPN; também gerencia pacotes `MIT`
* [delta](https://github.com/supershadoe/delta) ✨ - Gerenciador de hotspot usando o Shizuku `BSD-3-Clause`
* [Dolphy-App](https://github.com/unvoiddd/Dolphy-App) - Multiferramenta NFC, BLE e IR para pesquisa de protocolos sem fio `GPL-3.0`
* [EasySpot](https://github.com/EasySpotApp/EasySpot) - App que permite ligar o hotspot remotamente via Bluetooth; pense no Continuity da Apple, mas para todo mundo `GPL-3.0`
* [FindMyDevice](https://gitlab.com/fmd-foss/fmd-android) - Alternativa segura e de código aberto ao serviço FindMyDevice do Google. `GPL-3.0`
* [FireWall Blocks](https://github.com/shynoiddev/FireWall-Blocks) - Firewall de modo duplo: bloqueia o acesso à internet usando o Shizuku, uma interface VPN local padrão ou ambos. `MIT`
* [hikari-adblock](https://github.com/codegeasse1/hikari-adblock) - Bloqueador de anúncios/rastreadores/malware sem root, com filtro DNS por VPN local e modos de firewall iptables/nftables via Shizuku `GPL-3.0`
* [Hostman](https://github.com/LinZong/Hostman) `Root` - Visualiza e edita o arquivo /etc/hosts `MIT`
* [hotspot_channel_setter](https://github.com/Lorax121/hotspot_channel_setter) - Lista e aplica o canal 2,4/5 GHz do SoftAP do hotspot Wi-Fi via Shizuku ou root e mantém a escolha após reinicializações. `Proprietary`
* [MaybeEdgeScanner](https://github.com/maybeknott/MaybeEdgeScanner) - Scanner de rede com pareamento de rotas que testa alvos TCP/TLS/HTTP, com diagnóstico de rádio opcional assistido pelo Shizuku. `AGPL-3.0`
* [NaiveproxyForAndroid](https://github.com/Dobiec/NaiveproxyForAndroid) - App simples para rodar o Naiveproxy no Android `MIT`
* [NetManager](https://github.com/DottoXD/NetManager) - Monitor de rede celular em Material para 4G/5G NR, com mapa de torres, drive tests e testes de velocidade; uma ponte de shell Shizuku libera dados de rede extras. `GPL-3.0`
* [NetSwitcher](https://github.com/nd4y/netswitcher) - Alternância rápida entre Wi-Fi, dados móveis e Ethernet por app, atalho, widget ou bloco de configurações rápidas, usando Shizuku ou root. `Proprietary`
* [NetToggle](https://github.com/Dhangofa/NetToggle) - Bloco leve de Configurações rápidas para forçar os modos Somente 5G, Somente 4G e de rede preferencial usando Root ou Shizuku `GPL-3.0`
* [Network Scanner](https://github.com/usamaiqb/network-scanner) - Offline, privacy-focused scanner that discovers devices on your local network with hostnames, open ports and device types, using Shizuku or root to read the ARP table so MAC addresses and vendors show on Android 10+ `GPL-3.0`
* [NetworkSwitch](https://github.com/aunchagaonkar/NetworkSwitch) - App Android para alternar o modo de rede entre 4G/5G `GPL-3.0`
* [nobita](https://github.com/duhow/nobita) - Grava o tráfego Bluetooth HCI em arquivos PCAPNG compatíveis com o Wireshark no próprio aparelho, usando o Shizuku. `Proprietary`
* [Quintz](https://github.com/corgilittlelegs/Quintz) - Ferramenta sem root para travar a banda Wi-Fi e direcionar BSSID, que fixa o Android em 5/6 GHz via Shizuku, com telemetria de AP e um localizador de direção de RF. `MIT`
* [RKNHardering](https://github.com/xtclovver/RKNHardering) - Detecta no aparelho ferramentas de contorno por VPN/proxy usando verificações validadas pela comunidade, com sondagens privilegiadas via Shizuku ou Root. `AGPL-3.0`
* [ShizuWall](https://github.com/AhmetCanArslan/ShizuWall) ✨ - Firewall de apps de código aberto que não depende de VPN nem de root `GPL-3.0`
* [Shizzi](https://github.com/carlelieser/shizzi) - Contorno de bloqueio de tethering Wi-Fi sem root via Shizuku `Proprietary`
* [sing-box](https://f-droid.org/packages/io.nekohasekai.sfa/) - Plataforma universal de proxy. Usa o Shizuku para proxy por app `GPL-3.0` [(Código-fonte)](https://github.com/SagerNet/sing-box)
* [Traffic Light](https://play.google.com/store/apps/details?id=com.leekleak.trafficlight) - Medidor de velocidade de rede fixo na barra de status `GPL-3.0` [(Código-fonte)](https://github.com/leekleak/traffic-light)
* [WG Tunnel](https://github.com/wgtunnel/android) - Cliente Android livre para WireGuard e AmneziaWG com túnel automático. `MIT`
* [WiFi Portal](https://github.com/lovitus/wifiportal) - Aplica configurações de sondagem de portal cativo via Shizuku, com backup, verificação antes de gravar e predefinições regionais. `Proprietary`
* [wifi-password-manager](https://github.com/Khh-vu/wifi-password-manager) - App simples que usa o Shizuku para gerenciar e ver senhas de Wi-Fi salvas `MIT`
* [WiFiList](https://play.google.com/store/apps/details?id=tk.zwander.wifilist) `Paid` 💰 - Veja suas senhas de Wi-Fi salvas no Android 11 ou superior sem root `Proprietary` [(Código-fonte)](https://github.com/zacharee/WiFiList)

### Patching

* [LSPatch](https://github.com/JingMatrix/LSPatch) - Framework Xposed sem root derivado do LSPosed `GPL-3.0`
* [Morphe](https://morphe.software/) - Patcher de YouTube fácil de usar, baseado no Universal-ReVanced-Manager `GPL-3.0` [(Código-fonte)](https://github.com/MorpheApp/morphe-manager)
* [NPatch](https://github.com/7723mod/NPatch) ✨ - Framework Xposed sem root baseado no LSPosed, que injeta a API Xposed nos APKs alvo `GPL-3.0`
* [Universal-ReVanced-Manager](https://github.com/Jman-Github/Universal-ReVanced-Manager) - Patcher ReVanced com recursos extras que o gerenciador oficial não tem `GPL-3.0`

### Power management

* [Amply](https://github.com/d4rken-org/amply) - Controle fácil de limites de carga. Permite temporariamente uma carga completa e depois restaura automaticamente o seu limite de carga de proteção `GPL-3.0`
* [BatStats](https://github.com/mlm-games/BatStats) - Monitor de bateria com estatísticas via Shizuku `GPL-3.0`
* [Batt](https://gitlab.com/narektor/batt) - App simples que mostra informações de status da bateria no Android 14 ou superior. `GPL-3.0`
* [Battery](https://github.com/zhyang18/Battery/blob/main/README_EN.md) - Análise de saúde da bateria e do hardware; o Shizuku fornece o shell elevado para leituras profundas de parâmetros da bateria. `MIT`
* [Battery-Monitor](https://github.com/tswistak/Battery-Monitor) - Acompanha e registra a capacidade e os parâmetros da bateria ao longo do tempo usando o Shizuku `GPL-3.0`
* [battery-stats-changer](https://github.com/superisuer/battery-stats-changer) - App de código aberto para alterar visualmente os dados da bateria via Shizuku `GPL-3.0`
* [DozeTap](https://github.com/dhruvanbhalara/DozeTap) - Predefinições de tempo limite de tela que concedem WRITE_SECURE_SETTINGS com um toque pelo Shizuku. `Apache-2.0`
* [EnforceDoze](https://f-droid.org/packages/com.akylas.enforcedoze/) ✨ - Ativa o modo Doze logo após desligar a tela e desativa a detecção de movimento para obter a melhor duração de bateria `GPL-3.0` [(Código-fonte)](https://github.com/Akylas/EnforceDoze)
* [NoMoreBackground](https://f-droid.org/packages/com.adilhanney.no_more_background/) ✨ - Programa do tipo "configure e esqueça" para impedir que apps Android rodem em segundo plano `GPL-3.0` [(Código-fonte)](https://github.com/adil192/no_more_background)
* [PULSE // BATTERY](https://github.com/privshell/pulse-battery) - Relatório noturno de despertares por alarme de cada app, com restrição de standby verificada e reversível com um toque, além de diagnóstico de wake locks e alarmes, controles do Doze e backup de APK `MIT`
* [RebootNya](https://github.com/daisukiKaffuChino/RebootNya) - Menu de reinicialização avançado com suporte a Shizuku `Apache-2.0`
* [ScreenOff](https://github.com/WuDi-ZhanShen/ScreenOff) - Desliga a tela do Android sem entrar em modo de espera/suspensão `Proprietary`
* [sleep-timer](https://github.com/Xitee1/sleep-timer) - Timer de sono que pode pausar a mídia e desligar Wi-Fi/Bluetooth/tela `GPL-3.0`
* [USB PD Bypass](https://github.com/ONDER1E/usbpdbs) - Liga/desliga o modo de bypass de bateria do USB PD em limites de carga via Shizuku, com recuperação automática. `Proprietary`
* [volt](https://github.com/lebiggg/volt) - Sucessor do Greenify: hibernação de apps por pontuação, com despertar por push do UnifiedPush via Shizuku `GPL-3.0`
* [wakelogs](https://github.com/dernikiausd/wakelogs) - Analisa despertares da tela, atividade da CPU, alarmes e repouso do aparelho com diagnósticos do sistema baseados em Shizuku. `GPL-3.0`
* [zukulock](https://github.com/tiendnm/zukulock) - App bem leve que bloqueia a tela ao ser aberto. Ajuda a reduzir o desgaste do botão liga/desliga `MIT`

### Privacy

* [Amarok-Hider](https://apt.izzysoft.de/fdroid/index/apk/deltazero.amarok.foss) - Oculte seus arquivos privados e apps Android com um só clique `Apache-2.0` [(Código-fonte)](https://github.com/deltazefiro/Amarok-Hider)
* [AntiForensic-Tools](https://github.com/bakad3v/Android-AntiForensic-Tools) - App projetado para proteger silenciosamente os dados do usuário contra adversários poderosos `GPL-3.0`
* [anubis](https://github.com/sogonov/anubis) - Gerenciador de apps que congela/descongela grupos de apps conforme o estado da VPN via pm disable do Shizuku, para que apps congelados não consigam detectar nem contornar a VPN. `MIT`
* [AppLock](https://github.com/aload0/AppLock) ✨ - Bloqueia apps sensíveis com PIN e, opcionalmente, biometria `MIT`
* [AppOpsNext](https://github.com/1zumiii/AppOpsNext) - Gerenciador de AppOps para Android 15+, com modelos de permissão, alterações em lote, histórico de instalações e diagnósticos via Shizuku `GPL-3.0`
* [AvarionX-Android-Antivirus](https://github.com/phsycologicalFudge/AvarionX-Android-Antivirus) - Antivírus no próprio aparelho com verificação local de malware/APK, monitoramento de downloads e filtragem de DNS; o Shizuku viabiliza o monitoramento de comportamento típico de ransomware `MPL-2.0`
* [Monica](https://github.com/Monica-Pass/Monica) - Cofre de senhas Bitwarden/KeePass local em primeiro lugar, com TOTP; o Shizuku mantém a proteção do preenchimento automático rodando em segundo plano. `GPL-3.0`
* [Privacify](https://github.com/robinsrk/privacify) - Central de controle de privacidade: verificador de permissões, linha do tempo de uso de sensores e pontuação de privacidade, com controles avançados de hardware via Root/Shizuku. `Apache-2.0`
* [PrivacyFlip](https://f-droid.org/packages/io.github.dorumrr.privacyflip/) - Gerencia a privacidade do aparelho conforme o estado de bloqueio/desbloqueio `MIT` [(Código-fonte)](https://github.com/dorumrr/privacyflip)

### Productivity

* [Blink](https://github.com/character-flat/Blink) - Timer persistente e altamente personalizável para cuidado com os olhos pela regra 20-20-20, que usa o Shizuku para se colocar na lista de exceções das otimizações de bateria do Android `GPL-3.0`
* [Cresto](https://github.com/Nevodev/Cresto) - App de tarefas com captura por IA, sincronização de calendário e lembretes; sua extração da tela atual pelas Configurações rápidas captura a tela por acesso ao shell via Shizuku. `Apache-2.0`
* [Curbox](https://f-droid.org/packages/neth.iecal.curbox/) ✨ - Ferramenta para reduzir o vício em tela e ver análises de uso `GPL-3.0` [(Código-fonte)](https://github.com/curbox-app/curbox-android)
* [DetoxDroid](https://github.com/flxapps/DetoxDroid) - Detox digital: use o seu celular em vez de deixar que ele use você `GPL-3.0`
* [HyperCopy](https://github.com/1812z/HyperCopy) - Ferramenta que leva da área de transferência ao app, observando links copiados e abrindo-os direto no app certo via monitoramento por Shizuku ou LSPosed. `Proprietary`
* [input-leaf](https://github.com/anasvhora284/input-leaf) - Cliente Android para Input Leap/Deskflow: controle o celular com o mouse e o teclado do PC pela rede local usando injeção de entrada via Shizuku, sem root. `Apache-2.0`
* [quickdash](https://github.com/Balajitechlabs/quickdash) - Painel de produtividade flutuante com cobrança via UPI/PayPal e atalhos de chat; uma ponte Shizuku libera recursos privilegiados do sistema. `GPL-3.0`
* [Sefirah](https://github.com/shrimqy/Sefirah-Android) - Integração Windows-Android para sincronizar área de transferência, notificações, arquivos, SMS e chamadas; o Shizuku habilita a área de transferência no Android 10+. `GPL-3.0`

### Quick settings

* [AlwaysOnDisplayToggle](https://f-droid.org/packages/org.alberto97.aodtoggle/) - Ative/desative o Always on Display pelo painel de configurações rápidas `MIT` [(Código-fonte)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [Better Internet Tiles](https://play.google.com/store/apps/details?id=be.casperverswijvelt.unifiedinternetqs) - Traz de volta os blocos de Wi-Fi e dados móveis no Android 12 ou superior, além de um bloco de internet unificado melhor `GPL-3.0` [(Código-fonte)](https://github.com/CasperVerswijvelt/Better-Internet-Tiles)
* [DataSimTile](https://github.com/Mygod/DataSimTile) - Bloco para trocar o SIM padrão de dados móveis `Apache-2.0`
* [DisplayToggle](https://f-droid.org/packages/io.github.ulysseszh.displaytoggle/) - Oferece bloco de configurações rápidas e atalhos para desligar a tela sem bloqueá-la nem parar os apps em primeiro plano `MIT` [(Código-fonte)](https://github.com/UlyssesZh/DisplayToggle)
* [DNS Toggle](https://f-droid.org/packages/com.ericlowry.dnstoggle/) - Bloco de Configurações rápidas para ligar/desligar e configurar o DNS privado, com automação avançada opcional. `MIT` [(Código-fonte)](https://github.com/ELowry/DNSToggle)
* [ManualRotate](https://github.com/Verisonder/ManualRotate) - Bloco de configurações rápidas que alterna entre retrato/paisagem sem girar o celular; substituição opcional via Shizuku para apps que travam a orientação. `GPL-3.0`
* [Private DNS Quick Setting](https://apt.izzysoft.de/fdroid/index/apk/com.flashsphere.privatednsqs) - Bloco de configurações rápidas para ligar ou desligar o DNS privado `GPL-3.0` [(Código-fonte)](https://github.com/flashsphere/private-dns-qs)
* [PrivateDNSAndroid](https://github.com/karasevm/PrivateDNSAndroid) - Bloco de configurações rápidas para trocar o servidor de DNS privado ativo `MIT`
* [Quick-Tile Settings](https://f-droid.org/packages/com.rbn.qtsettings/) - Blocos de configurações rápidas para ligar/desligar a depuração USB e trocar os hosts de DNS privado `GPL-3.0` [(Código-fonte)](https://github.com/RBN-Apps/Quick-Tile-Settings)
* [SensorsOff](https://github.com/LinerSRT/SensorsOff) - Ativa/desativa os sensores do aparelho pelas configurações rápidas `Apache-2.0`
* [Tooler](https://github.com/jehan593/tooler) - Blocos de Configurações rápidas para tela de bloqueio, DNS privado, escala de cinza e carregamento, executados pelo Shizuku. `MIT`

### Software management

* [ADB Application Manager Pro](https://github.com/Bingblop/ADB-Application-Manager) - Gerenciador completo de apps e do dispositivo para debloat, congelar, instalar, fazer backup e ajustar configurações ocultas via Shizuku ou ADB. `Proprietary`
* [AppControlX](https://github.com/risunCode/AppControl-X) - Congele, force a parada, desinstale apps, altere a otimização em segundo plano e mais `GPL-3.0`
* [AppDualZuku](https://github.com/nathanatgit/AppDualZuku) - Gerencia várias instâncias de apps em espaços de trabalho isolados ou compartilhados (perfis gerenciados) usando Shizuku, com backend root opcional. `Proprietary`
* [AppManagerNG](https://github.com/SysAdminDoc/AppManagerNG) - Fork do [AppManager](https://github.com/muntashirakon/appmanager) para inspecionar, fazer debloat, backup, congelar e controlar apps Android; funciona com Shizuku, ADB, Dhizuku ou root. `GPL-3.0`
* [Appslim](https://github.com/Horizen5/Appslim/blob/master/docs/README_en.md) - Analisador de runtime Android que perfila o comportamento de inicialização, CPU/memória e chamadas Dex, e depois enxuga os apps por meio de hooks, regras e ações via Shizuku ou root. `Proprietary`
* [AppVaultX](https://github.com/sunilpaulmathew/AppVaultX) - Gerenciador de apps de alto desempenho movido pelo Shizuku `GPL-3.0`
* [Blocker](https://github.com/lihenggui/blocker) - Ative/desative componentes do Android como activities, services, receivers e providers `Apache-2.0`
* [Buge App Manager](https://github.com/BugeStudioTeam/Buge-App-Manager) - Um gerenciador de apps focado em gerenciamento de permissões `GPL-3.0`
* [Canta](https://play.google.com/store/apps/details?id=io.github.samolego.canta) ✨ - Desinstale qualquer app sem root `LGPL-3.0` [(Código-fonte)](https://github.com/samolego/Canta)
* [CloneCat](https://github.com/AhmetCanArslan/CloneCat) - Clone e gerencie apps entre perfil de trabalho, espaço privado, apps duplos e usuários secundários, com atalhos na tela inicial `Proprietary`
* [CloneSpace](https://github.com/udmodz0/adb-cloner) - Clonador de apps e espaço de trabalho multiusuário isolado movido pelo Shizuku, que executa cópias extras de apps em perfis separados sem duplicar APKs nem precisar de PC. `Apache-2.0`
* [Dexor](https://github.com/DeveshTone/Dexor) - Gerenciador de compilação antecipada (AOT) de bytecode e de dexopt em runtime para aplicativos Android `MIT`
* [DisabledLauncher](https://github.com/voruti/DisabledLauncher) - App Android que desativa apps não usados, mas ainda permite acessá-los com facilidade `MIT`
* [DroidUtility](https://github.com/DroidUtility/DroidUtility) - Conjunto de utilitários sem root para debloat, ajustes de sistema e execução de shell privilegiado via Shizuku, voltado a desenvolvedores que usam só o celular. `MIT`
* [FreezeYou](https://f-droid.org/packages/cf.playhi.freezeyou/) - Melhore a velocidade e a bateria do seu dispositivo congelando software ruim de forma manual ou semiautomática `Apache-2.0` [(Código-fonte)](https://github.com/FreezeYou/FreezeYou)
* [Hail](https://f-droid.org/packages/com.aistra.hail/) ✨ - Congele, oculte ou desative qualquer app. Crie e organize grupos de apps que podem ser congelados com um clique. `GPL-3.0` [(Código-fonte)](https://github.com/aistra0528/Hail)
* [Insular](https://f-droid.org/packages/com.oasisfeng.island.fdroid/) - Fork totalmente FLOSS do Island `Apache-2.0` [(Código-fonte)](https://gitlab.com/secure-system/Insular)
* [Inure App Manager](https://play.google.com/store/apps/details?id=app.simple.inure.play) `15-day trial` `IAP` 💰 - Gerenciador de apps Android para dispositivos com e sem root `GPL-3.0` [(Código-fonte)](https://github.com/Hamza417/Inure)
* [Island](https://play.google.com/store/apps/details?id=com.oasisfeng.island) - Isole e clone apps para proteção de privacidade e execução paralela `Apache-2.0` [(Código-fonte)](https://github.com/oasisfeng/island)
* [krude](https://github.com/KusStar/krude) - Launcher completo de apps e fluxos de trabalho `MIT`
* [Minimal Kernel Manager](https://github.com/zenithblue-oss/mkm) - Gerenciador de kernel e monitor de sistema com estatísticas de bateria, aplicação na inicialização e suporte a apps ocultos via Shizuku ou root. `GPL-3.0`
* [MMRL](https://github.com/MMRLApp/MMRL) `Root` - Gerencie seu repositório de módulos Magisk `GPL-3.0`
* [Package Manager](https://play.google.com/store/apps/details?id=com.smartpack.packagemanager) - Um app poderoso para gerenciar apps do sistema e do usuário `GPL-3.0` [(Código-fonte)](https://github.com/SmartPack/PackageManager)
* [Thor](https://play.google.com/store/apps/details?id=com.valhalla.thor) - Gerenciador de apps com recursos de congelamento e instalação. `GPL-3.0` [(Código-fonte)](https://github.com/trinadhthatakula/Thor)
* [UpgradeAll](https://f-droid.org/packages/net.xzos.upgradeall/) - Verifique atualizações de apps Android, módulos Magisk e mais! `GPL-3.0` [(Código-fonte)](https://github.com/DUpdateSystem/UpgradeAll)
* [User-Hopper](https://github.com/dlawoals2713/User-Hopper) - Create, start, stop and delete guest and secondary users on devices where the maker disabled multi-user support `GPL-3.0`
* [VOID // APPS](https://github.com/privshell/void-apps) - Gerenciador de apps via Shizuku: suspender, desativar, presets de debloat, permissões e AppOps, inicialização automática, bloqueio de rede por app, instalador de APK/XAPK e limpador. Toda alteração é conferida lendo de volta do Android `MIT`
* [Youki Users](https://github.com/mrYouki/Youki-Users) ✨ - Gerenciador multiusuário independente para Android, para criar, alternar e excluir perfis de usuário com fotos personalizadas. `GPL-3.0`

### Task manager

* [Android Monitor (Preview)](https://github.com/TerminalDev-1/AndroidMonitor-Preview) - Monitor de sistema no estilo Gerenciador de Tarefas com gráficos ao vivo de CPU, GPU, RAM, rede e temperatura; o Shizuku libera o uso real de CPU, a lista de processos e o Finalizar tarefa. `MIT`
* [KillMyApps](https://github.com/dedeadend/KillMyApps) - Finalizador de processos em segundo plano para melhorar a bateria e o desempenho via Shizuku ou root `GPL-3.0`
* [memhogs](https://github.com/cicerothoma/memhogs-android) - Quais apps estão consumindo a memória do seu celular. Detalhamento por app via Shizuku, com processos auxiliares agrupados sob o app a que pertencem `MIT`
* [MemorySnapshot](https://github.com/RyensX/MemorySnapshot/blob/master/docs/README_EN.md) - Observador de memória Android no próprio dispositivo: acompanhamento de PSS por app/processo, salvamento e comparação de snapshots, com dados coletados via Shizuku ou root. `Proprietary`
* [Pensum](https://github.com/troikoss/Pensum) ✨ - Gerenciador de Tarefas no estilo Windows para Android `GPL-3.0`
* [Pulse](https://github.com/xUmutKx/Pulse) - All-in-one toolbox built around a live task manager: CPU, memory, storage, network and temperature graphs, plus file explorer, silent installer, debloater, widgets and terminal `Proprietary`
* [ProcessLens](https://github.com/Dreamucxe/ProcessLens) - Observatório de processos que usa o Shizuku para leituras em nível de ADB de CPU, memória, threads, wake locks e bateria por app. `MIT`
* [ReAppzuku](https://github.com/gree1d/ReAppzuku) - Controle e gerencie aplicativos em segundo plano. Fork do shappky `GPL-3.0`
* [Recents](https://github.com/tymwitko/Recents) - Substituto do menu Recentes do sistema, independente do launcher, com suporte a finalizar apps via Shizuku `GPL-3.0`
* [Running Services Monitor](https://play.google.com/store/apps/details?id=me.biplobsd.rsm) - Monitore os serviços em execução no seu dispositivo Android `MIT` [(Código-fonte)](https://github.com/biplobsd/running_services_monitor)
* [RvSystem Monitor](https://github.com/Rve27/RvSystem-Monitor) - Monitor de sistema de alto desempenho (Compose + Rust) com informações de CPU e hardware obtidas via Shizuku `GPL-3.0`
* [shappky](https://github.com/YasserNull/shappky) ✨ - Um app simples para melhorar o desempenho parando apps em segundo plano. `GPL-3.0`
* [TaskManager](https://github.com/RohitKushvaha01/TaskManager) ✨ - Um Gerenciador de Tarefas para Android. Finalizar processos exige acesso root. `Apache-2.0`

### Terminals

* [aShell](https://gitlab.com/sunilpaulmathew/ashell) - Um shell ADB local para dispositivos Android com Shizuku `GPL-3.0`
  * [aShell You](https://github.com/DP-Hridayan/aShellYou) - Redesign do app aShell em Material You. `GPL-3.0`
* [Haven](https://f-droid.org/packages/sh.haven.app/) - Cliente de terminal, SSH, VNC, RDP, SFTP e armazenamento em nuvem para Android `AGPL-3.0` [(Código-fonte)](https://github.com/GlassHaven/Haven)

> [!NOTE]
> Usando o [rish](pages/RISH_pt-BR.md), você pode criar um shell ADB local com qualquer emulador de terminal, como o Termux.

### Vendor-specific

#### AYN
* [Heimdall-AYN-Thor-Assistant](https://github.com/mastercook777/Heimdall-AYN-Thor-Assistant) - Assistente de jogos na tela inferior do AYN Thor com perfis, macros, controles de toque, mapas e injeção de toque via Shizuku. `Apache-2.0`
* [Thor SidePad](https://github.com/bentolanh/thor-sidepad) - Transforma a tela inferior do AYN Thor em um gamepad virtual; o Shizuku injeta os toques como entrada nativa de controle. `MIT`
* [thor-pathfinder](https://github.com/KaitonGxx/thor-pathfinder) - Companheiro de tela dupla do AYN Thor: troca apps em execução entre as telas e mapeia atalhos de botões/combinações por perfil de jogo, usando o Shizuku para mover janelas para a outra tela. `GPL-3.0`
* [thor-wayfinder](https://github.com/Thor-Wayfinder/thor-wayfinder) - Move apps entre as duas telas do AYN Thor com gestos no botão voltar `CC-BY-NC-ND-4.0`
* [Thors-Lightning](https://github.com/HughesTechNZ/Thors-Lightning) - Controle de brilho das duas telas do AYN Thor pelo controle, com gravação opcional de entrada privilegiada via Shizuku. `MIT`
* [ThorVolumeLink](https://github.com/pth2000/ThorVolumeLink) - Controle de volume sincronizado para as duas telas do AYN Thor `MIT`

#### Google Pixel
* [Always On Display](https://f-droid.org/packages/org.alberto97.aodtoggle/) - Ative/desative o Always on Display pelo painel de configurações rápidas `MIT` [(Código-fonte)](https://github.com/Alberto97/AlwaysOnDisplayToggle)
* [carrier-ims-for-pixel](https://github.com/ryfineZ/carrier-ims-for-pixel) - Kit de IMS para Pixel com manutenção ativa: ajuste VoLTE/VoWiFi/VoNR, exibição de 5G e configuração da operadora via Shizuku `Apache-2.0`
* [hilight-studio](https://github.com/DhananjayBhosale/hilight-studio) - Controlador do LED HiLight do Pixel 11 para efeitos personalizados de luz de notificação e status `MIT`
* [Pixel-IMS-5G](https://github.com/barrylk/Pixel-IMS-5G) - Ative 5G standalone (5G SA) e VoNR em dispositivos Google Pixel `GPL-3.0`
* [pixel-volte-patch](https://github.com/kyujin-cho/pixel-volte-patch/blob/main/README.en.md) - Ative VoLTE no Pixel 6 e 7 com a LG U+ `GPL-3.0`
* [PixelCarrierSettings](https://github.com/iKirby/PixelCarrierSettings) - Ative VoLTE para operadoras em regiões não suportadas em dispositivos Pixel `GPL-3.0`
* [Root-My-Pixel](https://github.com/alex193a/Root-My-Pixel) - Automação de root para dispositivos Pixel via exploit CVE-2026-43499 `Proprietary`
* [Smartspacer](https://github.com/KieronQuinn/Smartspacer) - Widget personalizável, pode aprimorar o widget nativo 'Visão rápida' em dispositivos Pixel usando o Shizuku `GPL-3.0`
* [TensorIMS](https://github.com/Pixel-Tailor-CN/TensorIMS) - Ferramenta de configuração de IMS para dispositivos Pixel com Tensor; o Shizuku aplica os ajustes de VoLTE, VoWiFi, VT e VoNR. `Apache-2.0`
* [TurboIMS](https://github.com/Turbo1123/TurboIMS) - Ferramenta aprimorada de configuração de IMS para dispositivos Google Pixel `Apache-2.0`
* [Video Boost AO](https://github.com/AgusRomeroL/video-boost-ao) - Mantém o Video Boost ativado nas câmeras do Pixel Pro, reativando-o toda vez que a câmera é aberta. O Shizuku concede WRITE_SECURE_SETTINGS para o modo sob demanda `MIT`

#### Samsung OneUI

* [4Zones](https://github.com/mr-biz-apps/4zones) - Restaura a divisão de janelas em quatro zonas no Samsung DeX e no modo desktop do Android, com encaixe por toque e atalhos de teclado `Apache-2.0`
* [android-battery-health](https://github.com/willbilec/android-battery-health) - Visualizador de saúde da bateria e contagem de ciclos para Samsung, com layout amigável a leitores de tela, via Shizuku. `Proprietary`
* [duo-fold-live](https://github.com/joeconsorti/duo-fold-live) - Animação de dobra ao estilo iPhone-Duo, guiada pela dobradiça em tempo real, para o Galaxy Z Fold 8, com vidro em janelas, prévias ao vivo na tela externa e transição suave entre telas, lendo o ângulo real da dobradiça via Shizuku. `MIT`
* [Fonts](https://apt.izzysoft.de/fdroid/index/apk/com.je.fontsmanager.samsung) - Instalador de fontes sem root para One UI 8 `GPL-3.0` [(Código-fonte)](https://codeberg.org/dryerlint/fontsmanager)
* [galaxy-auto-brightness-offset](https://github.com/fullmetalsonic/galaxy-auto-brightness-offset) - Ajuste de deslocamento do brilho adaptável do Samsung Galaxy para telas que parecem escuras ou claras demais, inclusive com películas de privacidade: aplica uma correção fixa à curva de brilho automático via Shizuku. `Proprietary`
* [pearity](https://github.com/thejaustin/pearity) - Iguala as configurações do sistema do Samsung One UI aos padrões do iOS, um ajuste por vez (três estados: Android/Personalizado/iOS), gravando secure settings via Shizuku ou root. `Proprietary`
* [Root-My-Galaxy](https://github.com/BuSung-dev/Root-My-Galaxy) ✨ - Instalador do KSU para firmwares Samsung Galaxy suportados com CVE-2026-43499 `Apache-2.0`
* [SamsungRegionOverride](https://github.com/Ritel-T/SamsungRegionOverride) - Altere temporariamente a região do SIM vista pela Galaxy Store e outros apps com bloqueio regional, sem root, com restauração em um toque `MIT`
* [SBatteryTweaks](https://github.com/pascua28/SBatteryTweaks) - Ative ou desative o modo de carregamento rápido em dispositivos Samsung quando a temperatura da bateria atingir determinado ponto  `Proprietary`
* [ShutterMute](https://github.com/ajebulon/ShutterMute) - Desative o som obrigatório do obturador da câmera em dispositivos Samsung cujo CSC esteja definido para países com essa restrição `Proprietary`
* [SMTShell](https://github.com/BLuFeNiX/SMTShell) - Exploit de escalonamento de privilégios [(CVE-2019-16253)](https://nvd.nist.gov/vuln/detail/cve-2019-16253) para acesso como usuário de sistema (UID 1000) em dispositivos sem root com até OneUI 5. Usa o Shizuku para automação `LGPL-2.1`
* [ZFold-Multi-DPI](https://github.com/balamurugan15/ZFold-Multi-DPI) - Aplica presets separados de zoom de tela e DPI para a tela externa e a interna dos dispositivos Samsung Galaxy Z Fold `Proprietary`

#### MIUI

* [Aura](https://github.com/tgvdufuture/Aura) - App de LED de notificação RGB personalizado para o POCO X8 Pro, com cores e animações por app, por contato e por grupo `MIT`
* [CodecTweaker](https://github.com/Halo0sama/CodecTweaker) - Correção de codec Bluetooth para o Xiaomi HyperOS: restaura o codec e o bitrate escolhidos para cada fone após reconexões A2DP, usando Shizuku mais automação de interface por acessibilidade. `GPL-3.0`
* [FiveGSwitcher](https://play.google.com/store/apps/details?id=com.ysy.switcherfiveg) `Paid` 💰 - Atalho para ligar/desligar o 5G no HyperOS/MIUI `GPL-3.0` [(Código-fonte)](https://github.com/ysy950803/FiveGSwitcher)
* [FxxkMIUIAd](https://github.com/qhy040404/FxxkMIUIAd) - Desative os anúncios da MIUI com custo mínimo `Apache-2.0`
* [HyperOS FCM Fix](https://github.com/dingwen07/hyperos-fcm-fix) - Mantém o Google Play Services sem restrições no HyperOS para que as notificações push do FCM cheguem na hora `GPL-3.0`
* [HyperOS-MTZ-Studio](https://github.com/GloriousApps/HyperOS-MTZ-Studio/blob/main/readme_en.md) - Ambiente de trabalho de temas MTZ para o Xiaomi HyperOS; importa, compõe, traduz e aplica temas, usando Shizuku ou Shevery para aplicá-los sem root. `Proprietary`
* [HyperOS3ScrollSetter](https://github.com/BlizzardAn225/HyperOS3ScrollSetter) - Restaura os papéis de parede com rolagem e desativa o escurecimento forçado no HyperOS 3/4, aplicando secure settings e reinicializações via Shizuku.newProcess ou um módulo root. `GPL-3.0`
* [HyperOSUnfcker](https://github.com/Enki013/hyperosunfcker) - Desbloqueia configurações ocultas de desempenho, tela, memória, bateria e visual em dispositivos HyperOS/MIUI `LGPL-3.0`
* [IslandRecorder](https://github.com/wxxsfxyzm/IslandRecorder) - Gravador de tela focado em Xiaomi com controles na Super Island `GPL-3.0`
* [MixFlipTool](https://github.com/parallelcc/MixFlipTool) - Configuração em um clique da tela externa do Mix Flip: use qualquer app e restaure os apps do sistema ao estilo padrão `GPL-3.0`
* [NavigationSwitcher](https://github.com/chiyuki0325/NavigationSwitcher) - Ative a navegação por 3 botões em jogos de ritmo na MIUI / HyperOS  `Proprietary`

#### Nothing Phone
* [buttonoo](https://github.com/bractstudio/buttonoo) - Remapeia a Essential Key do Nothing para qualquer padrão de toque; o Shizuku habilita a rota de entrada privilegiada. `GPL-3.0`
* [GlyphBarty](https://github.com/Link2011-Act2/GlyphBarty) - Visualizador de Glyph personalizável para Nothing Phone com sincronização com música, botão nas Configurações rápidas e exibição do status de carregamento `MIT`
* [Recording-Light-Control](https://github.com/Farpathan/Recording-Light-Control) - O Recording Light Control oferece controle preciso da luz de gravação do Nothing Phone (3) `Proprietary`

#### Other

* [BooxUltimatum](https://github.com/huuunleashed/BooxUltimatum) - Conjunto de código aberto para tablets BOOX E Ink: tela inicial de alto contraste, telas de descanso, tinta instantânea da caneta, registro de bateria e ajustes reversíveis, usando o Shizuku para os níveis de ajuste privilegiados. `GPL-3.0`
* [Calibrate-SoC](https://github.com/mayusi/Calibrate-SoC) - Conjunto de ajuste, monitoramento e benchmark de SoC para portáteis de jogos Android, com governor orientado a metas e HUD ao vivo. `Apache-2.0`
* [DiAuto](https://github.com/shihabal3amri/DiAuto) - Receptor de Android Auto sem fio e por USB para centrais multimídia BYD DiLink; roda inteiramente na tela do carro e usa Shizuku ou root para a configuração privilegiada. Sem app companheiro no celular nem dongle. `AGPL-3.0`
* [Evolve_Launcher_v2](https://github.com/JarJarBlinkz/Evolve_Launcher_v2) - Launcher personalizável para headsets Meta Quest com organização de apps, registro de tempo de jogo e ações de limpar dados/cache via Shizuku. `Proprietary`
* [flipx](https://github.com/jlgrimes/flipx) - Direciona o botão home para launchers diferentes conforme o estado da dobradiça do Anbernic RG Rotate `Proprietary`
* [MindControl](https://github.com/Dinico414/MindControl) - Remapeador de botões físicos e kit de AOD para o iKKO MindOne, que monitora as teclas físicas via getevent do Shizuku, com alternativa por root. `Proprietary`
* [panel-assistant](https://github.com/panel-assistant/android) - Dashboard de painel de parede para Home Assistant com filtragem de entidades, controles de dispositivos MQTT e provisionamento e instalações verificadas via Shizuku/root. `Apache-2.0`
* [RedTrigger](https://github.com/zampierilucas/RedTrigger) - Gatilhos de ombro em todo o sistema para celulares Nubia Red Magic `MIT`
* [SuperBoox](https://github.com/rn-os/superboox) - Supernote-style swipe-in quick access panel for ONYX BOOX e-ink tablets with pinned notes and books, quick controls, clipboard history `Proprietary`

### Closed-source apps

Os apps de código fechado foram movidos para uma sublista separada. [Você pode vê-los aqui.](pages/CLOSED_SOURCE_pt-BR.md) 

> [!NOTE]
> **Por que os apps de código fechado ficam em uma lista separada?**
> O Shizuku dá aos apps acesso ADB de alto nível. Por segurança, este diretório principal inclui apenas apps de código aberto e de código disponível, pois qualquer pessoa pode conferir o código para garantir que não fazem nada suspeito e compilá-los na própria máquina.
>
> Apps totalmente fechados exigem confiança cega, por isso ficam em uma lista separada. 
> Quase todos os apps de código fechado já têm equivalentes de código aberto que implementam os mesmos recursos (quando não mais).

### Unlisted apps
Para manter a lista principal limpa, todos os apps descontinuados ou abandonados ficam em uma página separada: [ARCHIVED.md](pages/ARCHIVED.md)

> [!NOTE]
> Também uso um crawler automatizado que procura novos projetos que usam o Shizuku no GitHub e em vários repositórios F-Droid. Você pode ver o [relatório de crawl gerado automaticamente aqui](https://github.com/timschneeb/app-crawler/blob/master/SUMMARY.md).


--------------------

## Development libraries

### Core

* [Porter API](https://github.com/d4rken-org/porter-api) - SDK Android para o Porter, um fork do Shizuku com manutenção ativa, que oferece APIs compatíveis com o Shizuku e suporte direto ao Porter `MIT`
* [Shizuku-API](https://github.com/RikkaApps/Shizuku-API) - Documentação para desenvolvedores do Shizuku e do Sui, com exemplos `Apache-2.0`
* [Shizuku-API-Flutter-Plugin](https://github.com/runoob-coder/shizuku-api-flutter-plugin) - Um plugin Flutter para interagir com a API do Shizuku. `MIT`
* [Shizuku-Plugin (Flutter)](https://github.com/santhosh-D-subramani/Shizuku-Plugin) - Bindings da API do Shizuku para apps Flutter `GPL-3.0`

### Filesystem
* [Ackpine](https://github.com/solrudev/Ackpine) - Extensões de instalador de pacotes para Android, pensadas para Kotlin e compatíveis com Coroutines, com suporte ao Shizuku `Apache-2.0`
* [LintFile](https://github.com/lumkit/LintFile) - Uma biblioteca de operações de arquivo com backends Shizuku, root e sistema de arquivos comum `LGPL-2.1`
* [nextgenfs](https://github.com/rayshift/nextgenfs) - Acesso a android/data compatível com Shizuku a partir do Xamarin, biblioteca AIDL `MIT`


### System

* [droid-mcp](https://github.com/stixez/droid-mcp) - SDK Android que dá a apps de LLM/IA locais acesso estruturado, no próprio dispositivo, aos dados do celular, além de controle em nível de shell via Shizuku `Apache-2.0`
* [libterm](https://github.com/niki914/libterm) - Biblioteca de sessões de terminal para Android, pensada para Kotlin, com backends User, Root, Shizuku e SSH sob uma única API `Proprietary`
* [Priv Kit](https://github.com/priv-kit/priv-kit) - Biblioteca leve de runtime privilegiado para acesso a Binder via Root, ADB ou Shizuku no seu próprio app `Proprietary`

--------------------

## Miscellaneous content

### Command-line utilities

* [AndroSH](https://github.com/ahmed-alnassif/AndroSH) - Linux multidistro sem root no Android via Shizuku/ADB: rode Arch, Fedora, Alpine, Debian, Ubuntu, Kali, Void, Manjaro, OpenSUSE e Chimera com integração total ao sistema, isolamento proot e interface gráfica via Termux:X11 `GPL-3.0`

### Flows for [Automate](https://llamalab.com/automate/)

* [Better Shizuku Starter](https://llamalab.com/automate/community/flows/50863) - Verifica e inicia automaticamente o Shizuku **13.6** em eventos-chave via depuração sem fio com a versão *gratuita* do Automate. `MIT`
* [Shizuku Keeper](https://llamalab.com/automate/community/flows/51118) - Mantém o Shizuku **13.6** ou o **ADB** rodando sem interrupção, sem root, Wi-Fi ou cabos, via depuração USB com o Automate *Premium.* `MIT`
  * [Shizuku Keeper Lite](https://llamalab.com/automate/community/flows/51012) - Verifica o Shizuku **13.6** em intervalos regulares e o reinicia automaticamente via depuração sem fio com a versão *gratuita* do Automate. `MIT`
--------------------

## Annotations
- ✨ - Minha recomendação pessoal: faz uso intenso do Shizuku ou é uma pérola única/escondida
- `Paid` 💰 - Aplicativo pago
- `IAP` 💰 - Contém compras no app
- `Ads` - Contém anúncios
- `Proprietary` - Não licenciado sob uma licença FOSS. Vale para software de código fechado ou projetos de código disponível.
- `n-day trial` - Pagamento exigido após `n` dias
- `Root` - Exige que o Shizuku rode no modo Root

--------------------

## License

Esta lista está licenciada sob a licença [Creative Commons Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/deed.en).
