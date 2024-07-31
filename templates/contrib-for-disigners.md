
## Бейдж с основной статистикой:

Текущее разрещение:

	<width="300" height="280" fill="none">

Поля для отображаемой информации:

	Cyberrange Rating
    Username
    Total rating
    BugBounty rating
    Tolal score
    BugBounty score
    Cyberrange score
    BugBounty report count
    Cyberrange report count
    Vulnerability score 
    Business Risk score

 Идеально будет выделить значение Рейтинга киберполигона (Первая строка).
 Значения этих полей берутся из профилей пользователей и вытягиваются по ссылкам:

 	https://api.standoff365.com/api/bug-bounty/metrics/user/{USENAME}
 	https://api.standoff365.com/api/scoring-mgr/scoring/total/{USERNAME}

 Хотелось бы чтобы было 2 варианта этого бейджика
 - нормальный  (размерами схожим с текущим)
 - широкий  (шириной примерно в 800 пунктов)

## Бейдж с статистикой багбаунти:

Текущее разрещение:

	<width="300" height="300" fill="none">

Поля для отображаемой информации:

	BugBounty Rating
    Username
    Reports quality
    Reports impact
    Tolal report count
    Reports finished
    Reports in progress
    Accepted reports
    Informational
    Duplicate
    Out of scope
    Rejected
    Spam

Идеально будет выделить значение Рейтинга багбаунти (Первая строка). Значения этих полей берутся из профилей пользователей и вытягиваются по ссылкам:

 	https://api.standoff365.com/api/bug-bounty/metrics/user/{USENAME}
 	https://api.standoff365.com/api/scoring-mgr/scoring/total/{USERNAME}

## Прочее
Подробную информацию по собираемым метрикаам можно найти в этом репозитории:

	https://github.com/OohWhatever/STDstatistics/blob/main/templates/metrics.txt
либо у разработчиков сайта...

Последние актуальные бейджики можно найти вот здесь:
  

 	https://github.com/OohWhatever/STDstatistics/blob/main/templates/bb.svg
	https://github.com/OohWhatever/STDstatistics/blob/main/templates/common.svg 

## P.S.
Конкретных требований к дизайну как и и к размеру конечно же нет, feel free for contribute..
Главное чтобы было место под указанные метрики и было красиво...
