methods {
    getEvent(uint16) returns (address,uint64,uint16) envfree
    getNumEvents() returns (uint16) envfree
}

rule ticketsCanNeverUnderflow(method f, uint16 eventID) {
    env e;
    calldataarg args;

    address owner; uint64 ticketPrice; uint16 ticketsRemaining;
    owner, ticketPrice, ticketsRemaining = getEvent(eventID);
    f(e, args);
    uint16 currentTicketsRemaining;
    _, _, currentTicketsRemaining = getEvent(eventID);

    assert f.selector != createEvent(uint64,uint16).selector => currentTicketsRemaining <= ticketsRemaining;
    assert (currentTicketsRemaining < ticketsRemaining) =>
        (currentTicketsRemaining + 1 == ticketsRemaining) && 
        (f.selector == buyNewTicket(uint16,address).selector);
}

rule numEventsCanNeverDecrease(method f) {
    env e;
    calldataarg args;

    uint16 numEventsBefore = getNumEvents();
    f(e, args);
    assert numEventsBefore <= getNumEvents();
}

function eventUninitialized(uint16 eventID) returns bool {
    address owner;
    owner, _ , _ = getEvent(eventID);
    return owner == 0;
}

function eventStarted(uint16 eventID) returns bool {
    address owner;
    owner, _ , _ = getEvent(eventID);
    return owner != 0;
}

function eventClosed(uint16 eventID) returns bool {
    address owner; uint16 ticketsRemaining;
    owner , _ , ticketsRemaining = getEvent(eventID);
    return ticketsRemaining != 0;
}

rule eventStateFlow(method f, uint16 eventID) {
    env e;
    calldataarg args;

    // TODO not working
    require e.tx.origin != 0;

    bool uninitialized = eventUninitialized(eventID);
    bool started = eventStarted(eventID);
    bool closed = eventClosed(eventID);
    assert uninitialized && !started && !closed;
    assert !uninitialized && started && !closed;
    assert !uninitialized && !started && closed;
    f(e, args);

}