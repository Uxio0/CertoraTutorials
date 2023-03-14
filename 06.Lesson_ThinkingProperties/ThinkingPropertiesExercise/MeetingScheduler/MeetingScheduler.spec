methods {
    getStateById(uint256) returns (uint8) envfree
    getStartTimeById(uint256) returns (uint256) envfree
    getEndTimeById(uint256) returns (uint256) envfree
    getnumOfParticipants(uint256) returns (uint256) envfree
    getOrganizer(uint256) returns (address) envfree

    scheduleMeeting(uint256, uint256, uint256)
    startMeeting(uint256)
    cancelMeeting(uint256)
    endMeeting(uint256)
    joinMeeting(uint256) envfree
}

rule stateTransition(method f, uint256 meetingId) {
    calldataarg args;
    env e;

    uint8 previousState = getStateById(meetingId);
    f(e, args);
    uint8 currentState = getStateById(meetingId);

    assert (previousState == 0 && currentState == 1) => f.selector == scheduleMeeting(uint256, uint256, uint256).selector;
    assert (previousState == 1 && currentState == 2) => f.selector == startMeeting(uint256).selector;
    assert (previousState == 2 && currentState == 3) => f.selector == endMeeting(uint256).selector;
    assert (previousState == 2 && currentState == 4) => f.selector == cancelMeeting(uint256).selector;
}

rule numOfParticipantsIncrease(method f, uint256 meetingId) {
    calldataarg args;
    env e;

    require getStateById(meetingId) == 0 => getnumOfParticipants(meetingId) == 0;

    uint256 numOfParticipantsBefore = getnumOfParticipants(meetingId);
    f(e, args);
    uint256 currentNumOfParticipants = getnumOfParticipants(meetingId);

    assert (numOfParticipantsBefore != currentNumOfParticipants ) =>
            (f.selector == joinMeeting(uint256).selector) &&
            ((numOfParticipantsBefore + 1) == currentNumOfParticipants) &&
            (getStateById(meetingId) == 2);

}