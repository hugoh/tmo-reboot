# CHANGELOG

## v0.0.0 (2024-07-15)

### Unknown

* (build): Fix permissions (#3) ([`db87bc6`](https://github.com/hugoh/tmo-reboot/commit/db87bc66b65b91f9a8f275d723216086f7665ead))

* (chore): Add renovate.json (#2)

Co-authored-by: renovate[bot] &lt;29139614+renovate[bot]@users.noreply.github.com&gt; ([`490803d`](https://github.com/hugoh/tmo-reboot/commit/490803dea1dc6463a1f087da0fd820460df55347))

* (build): PyPI packaging

* Added super-linter

* Moved to Poetry

* Added semantic release ([`e69b2ec`](https://github.com/hugoh/tmo-reboot/commit/e69b2ecd100be57a8126c6d2b0c9e2d87cbc3c36))

* Merge branch &#39;highvolt-dev&#39;s main&#39; into tmo-reboot ([`52a5955`](https://github.com/hugoh/tmo-reboot/commit/52a595524ab4df41b8d3450350a232ce28be8a5d))

* Merge pull request #81 from highvolt-dev/enhancement/explicit_ipv4_ping

Enhancement/explicit ipv4 ping ([`dfc0d1a`](https://github.com/hugoh/tmo-reboot/commit/dfc0d1aeb5431b9f7f8f84a0728816755cde52a4))

* explicitly pass -4 flag to ping command to try ipv4 with ping command except for OS X clients, fixes #77 ([`938bb66`](https://github.com/hugoh/tmo-reboot/commit/938bb66901d5b2d2ef101caf8508c166df025c5a))

* correct README ([`84be2cb`](https://github.com/hugoh/tmo-reboot/commit/84be2cb980c48f79ed0942a022f3ff7184093f68))

* Merge pull request #80 from highvolt-dev/enhancement/alternative_connectivity_test

add support for alternative connectivity checks - fixes #13 #78 ; add… ([`7649a2b`](https://github.com/hugoh/tmo-reboot/commit/7649a2bf8966a7c329c103648f63d6ce015ab3cc))

* add support for alternative connectivity checks - fixes #13 #78 ; add explicit support for Sagecom gateway ([`bdddfa1`](https://github.com/hugoh/tmo-reboot/commit/bdddfa194e28201a2746bd507899f8157f5aa58e))

* Simplified cookies handling ([`fbd49ce`](https://github.com/hugoh/tmo-reboot/commit/fbd49ce18679f8edf903a93751a0c83f48c77549))

* Merge commit &#39;3ca7a447bfa37676f4bc13509fb33cdf50bb9216&#39; into tmo-reboot ([`cd20d99`](https://github.com/hugoh/tmo-reboot/commit/cd20d9904c5a04f4f1a3685d1c6e54e2f5ac5c61))

* Merge pull request #76 from highvolt-dev/bugfix/kvd21_5g_band_info

safely access 5g band info for arcadyan gateway - fixes #75 ([`3ca7a44`](https://github.com/hugoh/tmo-reboot/commit/3ca7a447bfa37676f4bc13509fb33cdf50bb9216))

* safely access 5g band info for arcadyan gateway - fixes #75 ([`cabbd3f`](https://github.com/hugoh/tmo-reboot/commit/cabbd3fa60454455b2d4d47bc6714bdae63ad9d4))

* Merge pull request #70 from highvolt-dev/bugfix/arcadyan_enbid_calculation

calculate arcaydyan eNB ID using decimal base fixes #68 caused by fir… ([`f5941ba`](https://github.com/hugoh/tmo-reboot/commit/f5941ba4e38ac69cc832efe7a574b0b5bfb18282))

* calculate arcaydyan eNB ID using decimal base fixes #68 caused by firmware update ([`9ba038a`](https://github.com/hugoh/tmo-reboot/commit/9ba038a36e6f47b676076053356324a6e6055963))

* Merge pull request #67 from highvolt-dev/bugfix/nokia_2104_bugfix

conditionally check for lsid cookie to avoid runtime error with nokia… ([`a87e6f1`](https://github.com/hugoh/tmo-reboot/commit/a87e6f11c16456f825680da06cf71c1e6e50d26e))

* conditionally check for lsid cookie to avoid runtime error with nokia 2104 firmware update ([`0626412`](https://github.com/hugoh/tmo-reboot/commit/0626412d2678db1f10646e02fcf2af4cb1133126))

* fix setting IPv6 ping via .env ([`25fa605`](https://github.com/hugoh/tmo-reboot/commit/25fa60505c4a3009407ce5dbc502d1382d016600))

* Merge pull request #62 from highvolt-dev/bugfix/ping6_bin_search

use ping6 binary if available for ipv6 ping functionality, fixes #43 ([`09b539a`](https://github.com/hugoh/tmo-reboot/commit/09b539a179ae709ff8276b509924ca62d9613796))

* use ping6 binary if available for ipv6 ping functionality, fixes #43 ([`6883b6b`](https://github.com/hugoh/tmo-reboot/commit/6883b6bda7a08c619087602f13cfb4ef7e36a6ee))

* Merge pull request #61 from highvolt-dev/feature/ping_v6_support

add IPv6 ping support, fixes #43 ([`1623b0c`](https://github.com/hugoh/tmo-reboot/commit/1623b0c09cd3b0603d35c7c73fe77adc08d8e028))

* add IPv6 ping support, fixes #43 ([`46b4ea0`](https://github.com/hugoh/tmo-reboot/commit/46b4ea0939da86633c367f0cc70314d9280be579))

* version bump ([`280b4b7`](https://github.com/hugoh/tmo-reboot/commit/280b4b75191d87df09b6021fa03278fdbbeaac0d))

* Merge pull request #57 from highvolt-dev/feature/bugfix_web_login_nokia

Feature/bugfix web login nokia ([`7c593d6`](https://github.com/hugoh/tmo-reboot/commit/7c593d634d62b17786b9e118e08f7396360eff6c))

* fixes #56 breaking change to webapp login after Nokia firmware upgrade to 1.2103.00.0338 ([`4bbe4e7`](https://github.com/hugoh/tmo-reboot/commit/4bbe4e727aa998ed205c0d6b4593e5bd54adf9cd))

* add missing import ([`f4fc36f`](https://github.com/hugoh/tmo-reboot/commit/f4fc36f60d2b5adec75dff973e90c05797c789b4))

* Merge pull request #55 from hugoh/log-to-syslog

Log to syslog ([`0174946`](https://github.com/hugoh/tmo-reboot/commit/017494631ef3fac88bcbb95c2963b927b32d32aa))

* Fixed missing leading space ([`3e30d99`](https://github.com/hugoh/tmo-reboot/commit/3e30d99ca8eb53f4e3f501a46c89e9ba94b9406f))

* Fixed out-of-scope use of syslog_socket ([`7e7e39e`](https://github.com/hugoh/tmo-reboot/commit/7e7e39ed7d599360994eb27aaf4a79cab529c5fc))

* Fixed log message format ([`87fcd7f`](https://github.com/hugoh/tmo-reboot/commit/87fcd7f48529e85a84435ea2f654d97e1c6e6771))

* Added support for Windows (untested) ([`dffe856`](https://github.com/hugoh/tmo-reboot/commit/dffe856c734bff9eabf215a37c47ada09bb4c2d6))

* Moved away from f-Strings to lower Python version requirement ([`e84d396`](https://github.com/hugoh/tmo-reboot/commit/e84d3965dcbab113c23859992e0d2f235996006a))

* Made Linux syslog logging work ([`c4c6f20`](https://github.com/hugoh/tmo-reboot/commit/c4c6f20e3489cc7621454d72e2d7848a1baa0e16))

* First commit to log to syslog - not working yet

Moved all the logging from print_and_log to logging, but syslog doesn&#39;t
work. Need to debug. ([`b6d73ff`](https://github.com/hugoh/tmo-reboot/commit/b6d73ff062e15e1078dd0d18cda3001563fe6def))

* First version of tmo-reboot ([`fa7976d`](https://github.com/hugoh/tmo-reboot/commit/fa7976da7d4fdfcdff7d3bb48495bdb94a61bfa2))

* add project logo ([`0c87853`](https://github.com/hugoh/tmo-reboot/commit/0c87853aacad5c623d982b7fdac4a7a165225cdb))

* Merge pull request #53 from highvolt-dev/feature/exit_status_codes

use meaningful exit status codes, fixes #52 ([`eff89e2`](https://github.com/hugoh/tmo-reboot/commit/eff89e22e892722aba23681f188c87a7ee85500b))

* clarify that a clean run will exit with status code 0 as expected ([`ad49203`](https://github.com/hugoh/tmo-reboot/commit/ad49203aa13f5f9a358e6a85f43e2e7dbb9b2731))

* use meaningful exit status codes, fixes #52 ([`0089e6d`](https://github.com/hugoh/tmo-reboot/commit/0089e6d24fdff19052a3daaea290d356e79a8b74))

* Update README.md

add Windows directions ([`f0bfebd`](https://github.com/hugoh/tmo-reboot/commit/f0bfebdec8202f7bb4df8c3b5d5716262825ed58))

* Merge pull request #51 from hugoh/fix-gateway-module-install

Fixed tmo_monitor.gateway module installation ([`37e3ed5`](https://github.com/hugoh/tmo-reboot/commit/37e3ed5e124490b2850b19dc40ae3999df6cd0f0))

* Fixed tmo_monitor.gateway module installation ([`3d1cfa1`](https://github.com/hugoh/tmo-reboot/commit/3d1cfa168ab122c036cf0d5f49b3f52eed05eae0))

* Update README.md

update description ([`2f07baf`](https://github.com/hugoh/tmo-reboot/commit/2f07baf1c25375e55da32c0b5cfa1670b63cf702))

* Merge pull request #47 from highvolt-dev/feature/kvd21_support

Feature/kvd21 support ([`5e049bb`](https://github.com/hugoh/tmo-reboot/commit/5e049bbb845af6845d79e2605574c02d4c06179b))

* change setup instructions ([`be3f594`](https://github.com/hugoh/tmo-reboot/commit/be3f594b93a3c3de34cfdc7dcdb27fc182046f26))

* implement rebooting for arcadyan gateway ([`db3f777`](https://github.com/hugoh/tmo-reboot/commit/db3f777a6c047de75ec01cd7389d59f67e60cb2d))

* add site info endpoint for arcadyan gateway ([`f04a21d`](https://github.com/hugoh/tmo-reboot/commit/f04a21d433615755ef20c601090338ad6f4a7f61))

* restructure project ([`0f5a7f5`](https://github.com/hugoh/tmo-reboot/commit/0f5a7f5060f701efa7541612276ddc3382905db5))

* initial work for KVD21 gateway support - enbid check and reboot not yet implemented ([`a619898`](https://github.com/hugoh/tmo-reboot/commit/a6198983c521ae6280e4301041ef775905856d5c))

* Merge pull request #46 from hugoh/busybox-ping

Support for Busybox&#39;s ping ([`0f43526`](https://github.com/hugoh/tmo-reboot/commit/0f4352678986afd444dfd0f1bd768ec55901df84))

* Support for Busybox&#39;s ping ([`690d54b`](https://github.com/hugoh/tmo-reboot/commit/690d54bc846cd809763c535bf2d7aa20ca11e713))

* Merge pull request #40 from AndrewPardoe/main

Fixes #34 ([`75c6523`](https://github.com/hugoh/tmo-reboot/commit/75c6523f79d0e5ee70997e4592aa7c94a962ee42))

* Bad reboot check prevented ping ([`472469d`](https://github.com/hugoh/tmo-reboot/commit/472469d76a34e69844053c72a1aa2e39b245e9b2))

* Fix for #34

Restore default behavior of reboot on 5g difference and ping ([`39c161b`](https://github.com/hugoh/tmo-reboot/commit/39c161b9697a359ac9285f2d2b893009ef3b2602))

* Merge pull request #39 from highvolt-dev/bugfix/osx_ping_parsing

Bugfix/osx ping parsing ([`72a9a08`](https://github.com/hugoh/tmo-reboot/commit/72a9a0874e716b0c5c7b5f69d788a8991a26ed05))

* fix regex syntax - use non-capturing group instead of character class ([`79e6724`](https://github.com/hugoh/tmo-reboot/commit/79e672478b4c39bfb31b6e684d877ce4ac84918e))

* Merge pull request #36 from delikat/delikat/fix-macos-ping-parsing

Support macOS ping output format ([`79cc739`](https://github.com/hugoh/tmo-reboot/commit/79cc739858d74beab08c26fdfb5d332e141d6113))

* Trim added whitespace ([`8324f86`](https://github.com/hugoh/tmo-reboot/commit/8324f86dd2ef357b9aba3e08356c290695fb47b6))

* Support macOS ping output format ([`0a2a47c`](https://github.com/hugoh/tmo-reboot/commit/0a2a47c001f03a791669f2543b09f18e301b4094))

* Merge pull request #38 from highvolt-dev/bugfix/requirements_cleanup

Bugfix/requirements cleanup ([`cbc3d8b`](https://github.com/hugoh/tmo-reboot/commit/cbc3d8baf6cded84ff8968030f71d4eb7803428e))

* base requirements.txt on 1.0 branch and add parse, python-dotenv, and tailer ([`a1d47c2`](https://github.com/hugoh/tmo-reboot/commit/a1d47c29bca50b5eac3438eff0efbb42ce486244))

* Merge pull request #33 from AndrewPardoe/requirements

Regenerated requirements.txt with pipreqs ([`c8a2874`](https://github.com/hugoh/tmo-reboot/commit/c8a28749313ad09c0dcb3b3a210d72067bd11ad3))

* Regenerated requirements.txt with pipreqs ([`54ceb4d`](https://github.com/hugoh/tmo-reboot/commit/54ceb4d0ebf249d48ab56d80cf247ec5648ab549))

* fix multiple bugs discovered in #31 ([`9e2df70`](https://github.com/hugoh/tmo-reboot/commit/9e2df70aff5e985970e606cd32f2fd11b35f8129))

* clarify that ping count performs as few pings as necessary ([`8cb8dff`](https://github.com/hugoh/tmo-reboot/commit/8cb8dffd65a64421117d427684c196c631a65d55))

* remove trailing whitespace ([`42ab29d`](https://github.com/hugoh/tmo-reboot/commit/42ab29dc2dd646025a70830e6cc79f39508c270f))

* Update README formatting

Add missing line breaks to fix malformed general option formatting, add colons for consistency ([`53bdf03`](https://github.com/hugoh/tmo-reboot/commit/53bdf037c45cbb9b407db5aab7e16624db5be205))

* Merge pull request #30 from AndrewPardoe/main

Address the feedback from #24 ([`04b15a1`](https://github.com/hugoh/tmo-reboot/commit/04b15a1610b3bba6f536b13de1e36f6c27c4c766))

* NFC ([`8261a49`](https://github.com/hugoh/tmo-reboot/commit/8261a49f84a0c054d012bb15bec8313a19529eb9))

* Address feedback in #24

Squashed commit of the following:

commit b1a388c4364ddf5998c93d431c8bd77c367680d9
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Fri Dec 31 09:50:27 2021 -0800

    Add print_and_log function

commit fe673487bde3ca3768a67ef633bc09595b95f6d3
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Fri Dec 31 09:21:29 2021 -0800

    Add logging options to command line &amp; README

    Also add back early ping success check for Windows. ([`0fb19cb`](https://github.com/hugoh/tmo-reboot/commit/0fb19cb38cfda68b20fe3da84b2890d4933343d9))

* Merge pull request #24 from AndrewPardoe/main

Add basic logging functionality &amp; log all connection metrics ([`ae9d264`](https://github.com/hugoh/tmo-reboot/commit/ae9d2643459aaf92d48f898ff0fb8f22af69505e))

* Add delta logging. Squashed commit of the following:

commit 4cc7fa66ba04dd4f188f6441b64c14a71737b0b9
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Tue Dec 28 07:56:53 2021 -0800

    Cleanup small delta logging items

commit 22d1c60d163e05608c3337a22c70c376e9a73f65
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Mon Dec 27 07:58:36 2021 -0800

    Add option to force log write from command line

    This option&#39;s nice when you&#39;re watching your log like a boiling pot

commit 83bc38295cecd1a7c5972c3cfbe8652457597ea6
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Sun Dec 26 08:58:36 2021 -0800

    Correct indentation error: `data` out of scope

commit c05700dcfe1fdd4f76b0a2d4186aeffca7c75909
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Sun Dec 26 08:47:04 2021 -0800

    Update requirements for tailer &amp; parse

commit e31d0796751a9caa3b74b3f2ecfa4aa52712d56e
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Sun Dec 26 08:42:41 2021 -0800

    Add delta logging ([`bec4522`](https://github.com/hugoh/tmo-reboot/commit/bec452240c3bec471c59b980313b83b29ea619df))

* Squashed commit of the following:

commit 3c1b750c4ec3276ad228108dabe2f82a08fc6210
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Fri Dec 24 09:13:15 2021 -0800

    Add basic logging and connection logging

    Add new logging options:
      - tmo_logfile: specify logfile
      - tmo_log_all: log all connection statistics

    Also move some error output to logfile

commit fd85144231eaf7b93a4bec50ee423d401d68ef1b
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Tue Dec 21 16:23:51 2021 -0500

    Add default operational logging

    1. Move error messages from print to logging.error
    2. Add operational logging
    3. Add log_all option to log all connection characteristics

commit cb5eefdbaecaec8391d9c8376eeb4ddf8d2d49b4
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Mon Dec 20 22:25:43 2021 -0500

    Added logging for basic cases ([`21e29e9`](https://github.com/hugoh/tmo-reboot/commit/21e29e93b26c50c31cb289faeb50c1faeaa846e1))

* Merge pull request #23 from AndrewPardoe/v2

v2: Add .env file for configuration &amp; rework args ([`fceb95f`](https://github.com/hugoh/tmo-reboot/commit/fceb95f69310bf6bc27e8bf64314a2abf79b99fe))

* Addressing feedback for PR 23 ([`a93cdc7`](https://github.com/hugoh/tmo-reboot/commit/a93cdc7a67deba780cf1449275c233c7bcbcefa0))

* v2: Add .env file for configuration &amp; rework args

Add .env file for configuration settings
Rework arguments &amp; argument parsing
Add try/catch around `request.get` that require connection

Squashed commit of the following:

commit 1ad90f8da3a3908ffd5737ccd07318a40164e97b
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Thu Dec 16 17:33:35 2021 -0800

    tolower the True comparisons

commit b4d0df17f99f1bf819c1002f7832f18d2cd0c212
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Thu Dec 16 17:28:04 2021 -0800

    Try/catch around get requests

commit e9dd8e7de49b73cb7c4449ecc80b072a655f0b75
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Thu Dec 16 16:13:44 2021 -0800

    Re-enabled reboot function

commit ec1347f7bc346e60f188fd2e319bbcee3de2484d
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Thu Dec 16 16:12:35 2021 -0800

    Finished testing of configuration

commit 5f7251a46e344f291f217191bb7e1e7887358854
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Wed Dec 15 08:19:40 2021 -0800

    Add small design spec for v2

commit 14c1badc2a9b805d561fbc65f023aaaa35f34c86
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Sun Dec 12 19:12:53 2021 -0800

    Add eND ID info to output

commit 368ca2c1d295b9107014b11a00d36a351d39699a
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Sun Dec 12 16:46:55 2021 -0800

    Support new ping parameters &amp; update requirements

commit 686ba2e04f8420edf8d5f362184aec0500719f68
Author: Andrew Pardoe &lt;AndrewPardoe@users.noreply.github.com&gt;
Date:   Sun Dec 12 16:04:18 2021 -0800

    Add .env support for config &amp; refactor arg parsing ([`356d422`](https://github.com/hugoh/tmo-reboot/commit/356d422cc9f83118ac82cbae156d5c6ebf837d9d))

* add support for multiple ping checks, rebooting only if all fail - fixes #19 ([`d8965e6`](https://github.com/hugoh/tmo-reboot/commit/d8965e6e6bba21b0f085187c7b7a5d9efa3fa211))

* Merge pull request #16 from BenKesselring/refactor-into-a-class

move everything into a tidy class for easier handling of user/pass and logins ([`a9a4076`](https://github.com/hugoh/tmo-reboot/commit/a9a407602cc032c9d68e94838428bd7c97db790f))

* move everything into a tidy class for easier handling of user/pass and logins ([`1410e42`](https://github.com/hugoh/tmo-reboot/commit/1410e42fe637832fea703aa604184579092a20be))

* Update README.md

update project summary ([`572b7a0`](https://github.com/hugoh/tmo-reboot/commit/572b7a0a15791aebad47a27da685ea8ca5afe9e2))

* Merge branch &#39;main&#39; of github.com:highvolt-dev/tmo-monitor into main ([`bb16007`](https://github.com/hugoh/tmo-reboot/commit/bb1600761f210f3ee8fcd8381426081e1bafd98a))

* Update README.md

Remove extraneous text from `--uptime` flag description ([`994d2ed`](https://github.com/hugoh/tmo-reboot/commit/994d2ed1a9fd26f2c4d2f849b408f7ca04db3f12))

* add support for checking eNB ID ([`83a71b0`](https://github.com/hugoh/tmo-reboot/commit/83a71b03a73981409d346fdcd185a238fae3a56e))

* add uptime threshold check - fixes #10 ([`761645a`](https://github.com/hugoh/tmo-reboot/commit/761645afdbf0c23ca7e3b00ec416b5c36971cd1b))

* update README and help prompts with defaults ([`e2189f6`](https://github.com/hugoh/tmo-reboot/commit/e2189f66b86a19a31b377880e5305146c0243cca))

* specify default ping host ([`565410e`](https://github.com/hugoh/tmo-reboot/commit/565410e53175e4931378a8bd3d852a08008a2d15))

* add Windows support ([`3e77ce0`](https://github.com/hugoh/tmo-reboot/commit/3e77ce0488bdf30699d2a8d67fbd2d638d8c2efa))

* remove unnecessary print of args ([`575e4dd`](https://github.com/hugoh/tmo-reboot/commit/575e4ddeb961b3ac248453380e70b62ff8094bd9))

* clarify ping host usage ([`070e6d3`](https://github.com/hugoh/tmo-reboot/commit/070e6d35f201c5d4821801a068e2311c1be77555))

* specify default 5g band ([`1455871`](https://github.com/hugoh/tmo-reboot/commit/14558710dddbc12ed1af50a75ddf9a27c097a005))

* add flags to skip rebooting, skip checking 5g bands, specify allowed 4g bands, and specify allowed 5g bands ([`721ce5d`](https://github.com/hugoh/tmo-reboot/commit/721ce5db53334a1667a63a483595654a9b203b35))

* add option to skip ping check ([`05ce8d0`](https://github.com/hugoh/tmo-reboot/commit/05ce8d0ba60dcbd6b3d22f9a8aa7aa6eee792c92))

* add option for skipping connected band check ([`eac5c11`](https://github.com/hugoh/tmo-reboot/commit/eac5c11fdb172ea3f15946cbeeed459f564f1684))

* improve compatibility for mixed python 2/3 environments ([`e8579f4`](https://github.com/hugoh/tmo-reboot/commit/e8579f4daf27c721c07c89327bb7fb7f0f4f1eac))

* minor formatting updates in README ([`104be95`](https://github.com/hugoh/tmo-reboot/commit/104be9582db581d166086f6167491ff77702091f))

* correct mistake in pip install command in README ([`64e669c`](https://github.com/hugoh/tmo-reboot/commit/64e669c4408efb365f86dc88c88cb3100d4fbd3c))

* Merge pull request #2 from BenKesselring/feature-immediate-reboot

update README to reflect new --reboot argument ([`3cddf6b`](https://github.com/hugoh/tmo-reboot/commit/3cddf6bf82bebe474bf8e9be9e808bb7a6654567))

* update README to reflect new --reboot argument ([`edc32b0`](https://github.com/hugoh/tmo-reboot/commit/edc32b0cfda329637ffcabd5d7f7dfe8b2135f5d))

* Merge pull request #1 from BenKesselring/feature-immediate-reboot

feature: add ability to skip health checks and immediately reboot gateway ([`2507ddb`](https://github.com/hugoh/tmo-reboot/commit/2507ddbdac153139b17e44de1ca0fd53c15bd895))

* feature: add ability to skip health checks and immediately reboot gateway

Add `--reboot` argument to force a reboot of the gateway and skip the health checks (for use in, say, a nightly cronjob to reboot the gateway regardless of connection status) ([`3e4d214`](https://github.com/hugoh/tmo-reboot/commit/3e4d2147d5b5c7c0d6493a92624fd2ef9e2e203f))

* Create README.md ([`b907555`](https://github.com/hugoh/tmo-reboot/commit/b907555a4a5800b305141f19c1e3523927c38d8d))

* initial commit ([`9a98914`](https://github.com/hugoh/tmo-reboot/commit/9a98914c674ccc74fc63f44b771854a29b18e53f))

* Initial commit ([`d97779b`](https://github.com/hugoh/tmo-reboot/commit/d97779b84c55c13fd766e794089d999317ffeab3))
