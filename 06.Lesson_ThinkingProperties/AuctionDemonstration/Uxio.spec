methods {
    getAuction(uint) returns (uint,uint,address,uint,uint) envfree
}

function getPrize(uint auctionId) returns uint {
    uint prize; uint payment; address winner; uint bid_expiry; uint end_time;
    prize, payment, winner, bid_expiry, end_time = getAuction(auctionId);
    return prize;
}
function getPayment(uint auctionId) returns uint {
    uint prize; uint payment; address winner; uint bid_expiry; uint end_time;
    prize, payment, winner, bid_expiry, end_time = getAuction(auctionId);
    return payment;
}
function getWinner(uint auctionId) returns address {
    uint prize; uint payment; address winner; uint bid_expiry; uint end_time;
    prize, payment, winner, bid_expiry, end_time = getAuction(auctionId);
    return winner;
}
function getBidExpiricy(uint auctionId) returns uint {
    uint prize; uint payment; address winner; uint bid_expiry; uint end_time;
    prize, payment, winner, bid_expiry, end_time = getAuction(auctionId);
    return bid_expiry;
}
function getEndtime(uint auctionId) returns uint {
    uint prize; uint payment; address winner; uint bid_expiry; uint end_time;
    prize, payment, winner, bid_expiry, end_time = getAuction(auctionId);
    return end_time;
}

definition auctionClosed(uint auctionId) returns bool =
    getPrize(auctionId) == 0 && getPayment(auctionId) == 0 && getWinner(auctionId) == 0x0000000000000000000000000000000000000000 && getBidExpiricy(auctionId) == 0 && getEndtime(auctionId) == 0 ;

definition auctionStarted(uint auctionId) returns bool =
    getEndtime(auctionId) > 0;


rule stateFlow(method f, uint auctionId) {
    // Auctions can only be started by newAuction method
    env e;
    calldataarg args;

    uint prize; uint payment; address winner; uint bid_expiry; uint end_time;
    prize, payment, winner, bid_expiry, end_time = getAuction(auctionId);
    bool closed = prize == 0 && payment == 0 && bid_expiry == 0 && end_time == 0 && winner == 0x0000000000000000000000000000000000000000;
    f(e, args);
    bool opened = end_time > 0;
    assert closed && opened => f.selector == newAuction(uint,uint).selector;
}