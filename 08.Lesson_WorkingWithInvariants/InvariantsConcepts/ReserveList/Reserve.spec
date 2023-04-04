methods {
    getTokenAtIndex(uint256) returns (address) envfree
    getIdOfToken(address) returns (uint256) envfree
    getReserveCount() returns (uint256) envfree
    addReserve(address,address,address,uint256) envfree
    removeReserve(address token) envfree
	reserves(address) returns (uint256, address, address, address, uint256) envfree
	underlyinglist(uint256) returns (address) envfree
}

//invariant bothListsCorrelated(uint256 tokenId, address token)
//	(tokenId != 0 && token != 0 => (getTokenAtIndex(tokenId) == token <=> getIdOfToken(token) == tokenId)) &&
//	(tokenId == 0 => (getTokenAtIndex(tokenId) == token => getIdOfToken(token) == tokenId))

	
invariant noTokenSavedIndexGreaterCounter(address token)
	(getReserveCount() == 0 => getIdOfToken(token) == 0)
	&&
	(getReserveCount() > 0 => getIdOfToken(token) < getReserveCount())
	{
		preserved removeReserve(address t) {
				require t == token;
			}
	}
