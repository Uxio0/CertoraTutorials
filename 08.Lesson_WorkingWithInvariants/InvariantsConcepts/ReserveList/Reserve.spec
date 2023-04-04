methods {
    getTokenAtIndex(uint256) returns (address) envfree
    getIdOfToken(address) returns (uint256) envfree
    getReserveCount() returns (uint256) envfree
    addReserve(address,address,address,uint256) envfree
    removeReserve(address token) envfree
}

invariant noTokenSavedIndexGreaterCounter(address token)
	(getReserveCount() == 0 => getIdOfToken(token) == 0)
	&&
	(getReserveCount() > 0 => getIdOfToken(token) < getReserveCount())
	{
		preserved removeReserve(address t) {
				require t == token;
			}
	}


invariant bothListsCorrelated(uint256 tokenId, address token)
	(tokenId != 0 && token != 0 => (getTokenAtIndex(tokenId) == token <=> getIdOfToken(token) == tokenId)) &&
	(tokenId == 0 => (getTokenAtIndex(tokenId) == token => getIdOfToken(token) == tokenId))

	{
		preserved {
			requireInvariant noTokenSavedIndexGreaterCounter(token);
		}

		preserved removeReserve(address t) {
				require t == token;
		}
	}


invariant nullTokenCannotBeStored(address token)
	(token == 0) => getIdOfToken(token) == 0

invariant tokenIdInjective(address token, address token2)
	((token != token2) && (getIdOfToken(token) == getIdOfToken(token2))) => getIdOfToken(token) == 0
	{
		preserved {
			// Lists in storage must be correlated for this invariant to work
			requireInvariant bothListsCorrelated(getIdOfToken(token), token);
			requireInvariant bothListsCorrelated(getIdOfToken(token2), token2);
		}
	}
