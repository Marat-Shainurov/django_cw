### Описание задач

- Реализуйте интерфейс заполнения рассылок, то есть CRUD механизм для управления рассылками.
- Реализуйте скрипт рассылки, который работает как из командой строки, так и по расписанию.
- Добавьте настройки конфигурации для периодического запуска задачи.

### Сущности системы

- Клиент сервиса:
    - контактный email
    - фио
    - комментарий
- Рассылка (настройки)
    - время рассылки
    - периодичность: раз в день, раз в неделю, раз в месяц
    - статус рассылки (завершена, создана, запущена)
- Сообщение для рассылки
    - тема письма
    - тело письма
- Попытка рассылки
    - дата и время последней попытки
    - статус попытки
    - ответ почтового сервера, если он был

<aside>
ℹ️ **Примечание:**
Не забудьте про связи между сущностями. Вы можете расширять модели для сущностей в произвольном количестве полей, либо добавлять вспомогательные модели.

</aside>

### Логика работы системы

- После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания - должны быть
  выбраны из справочника все клиенты, которые указаны в настройках рассылки и запущена отправка для всех этих клиентов.
- Если создаётся рассылка с временем старта в будущем - отправка должна стартовать автоматически по наступлению этого
  времени без дополнительных действий со стороны пользователя системы.
- По ходу отправки сообщений должна собираться статистика (см. описание сущности "сообщение" и "попытка" выше) по
  каждому сообщению для последующего формирования отчётов.
- Внешний сервис, который принимает отправляемые сообщения, может долго обрабатывать запрос, отвечать некорректными
  данными, на какое-то время вообще не принимать запросы. Нужна корректная обработка подобных ошибок. Проблемы с внешним
  сервисом не должны влиять на стабильность работы разрабатываемого сервиса рассылок.

<aside>
👨🏻‍💻 **Рекомендации**

- реализовать интерфейс можно с помощью uikit Bootstrap
- для работы с периодическими задачами можно использовать либо crontab задачи в чистом виде, либо изучить дополнительно
  библиотеку https://pypi.org/project/django-crontab/

</aside>

## Этап 2. Доработка сервиса

<aside>
📍 Сервис по управлению рассылками пользуется популярностью и запущенный MVP уже не удовлетворяет потребностям бизнеса. 

Вам нужно доработать сервис, чтобы он стал доступен для использования различными клиентами. А также сделать доработки
для развития сервиса в интернете.

</aside>

### Описание задач

- Расширьте модель пользователя для регистрации по почте, а также верификации
- Добавьте интерфейс для входа, регистрации и подтверждения почтового ящика
- Реализуйте ограничение доступа к рассылкам для разных пользователей
- Реализуйте интерфейс менеджера
- Создайте блог для продвижения сервиса

<aside>
ℹ️ **Примечание:**
Используйте для наследования модель `AbstractUser`

</aside>

### Функционал менеджера

- **может** просматривать любые рассылки
- **может** просматривать список пользователей сервиса
- **может** блокировать пользователей сервиса
- **может** отключать рассылки
- **не может** редактировать рассылки
- **не может** управлять списком рассылок
- **не может** изменять рассылки и сообщения

### Функционал пользователя

Весь функционал дублируется из старой версии, но теперь нужно следить за тем, чтобы пользователь не мог случайным
образом изменить чужую рассылку и мог работать только со своим списком клиентов и со своим списком рассылок.

## Продвижение

### Блог

Реализуйте приложение для ведения блога. При этом, отдельный интерфейс реализовывать нет необходимости, но настроить
административную панель для контент-менеджера необходимо. В сущность блога добавьте следующие поля:

- заголовок
- содержимое статьи
- изображение
- количество просмотров
- дата публикации

### Главная страница

Реализуйте главную страницу в произвольном формате, но обязательно отобразите следующую информацию:

- количество рассылок всего
- количество активных рассылок
- количество уникальных клиентов для рассылок
- 3 случайные статьи из блога

Для блога и главной страницы самостоятельно выберите какие данные необходимо кешировать, а также каким способом
необходимо произвести кеширование.

### Критерии приемки

- [ ]  Интерфейс системы содержит следующие экраны: список рассылок, отчет проведенных рассылок отдельно, создание
  рассылки, удаление рассылки, создание пользователя, удаление пользователя, редактирование пользователя
- [ ]  Реализована вся требуемая логика поведения
- [ ]  Интерфейс понятен и соответствует базовым требованиям системы
- [ ]  Все интерфейсы, не относящиеся к стандартной админке, для изменения и создания сущностей необходимо реализовать с
  помощью Django форм
- [ ]  Все настройки прав доступа реализованы верно
- [ ]  Использовано как минимум два типа кеширования
- [ ]  Решение выложено на [github.com](http://github.com/)