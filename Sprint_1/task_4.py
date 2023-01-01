types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


def dedup(tickets):
    # сортировка нужна для старого питона, в python3.* словари по умолчанию OrderedDict
    # проходим по тикетам снизу вверх и определяем его приоритет
    # в обратном порядке для того, чтобы у API_45 приоритет был 1, а не 3
    return {
        ticket: priority
        for priority, priority_tickets in sorted(tickets.items(), key=lambda ticket: ticket[0], reverse=True)
        for ticket in priority_tickets
    }


def tickets_with_priorities(types, ticket_priorities):
    result = {}

    for ticket, type in sorted(ticket_priorities.items(), key=lambda ticket_priority: ticket_priority[1]):
    # Будет круто, если вы расскажете, как ваш же коммент должен использоваться здесь, потому что я всадил
    # суммарно часов восемь в попытке переделать рабочее решение (зачем-то) и не хочу больше тратить время
        try:
            result[types[type]].append(ticket)
        except KeyError:
            result[types[type]] = [ticket]

    return result
