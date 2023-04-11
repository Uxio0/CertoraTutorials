// #contract ArrayImproved.sol:Array
methods {
    get(uint) returns (address) envfree
    getWithDefaultValue(uint) returns (address) envfree
    isListed(address) returns (bool) envfree
    getLength() returns (uint) envfree
}


invariant uniqueArrayUsingRevert(uint256 i, uint256 j)
(
    (getWithDefaultValue(i) == getWithDefaultValue(j)) => (i == j) || (getWithDefaultValue(i) == 0)
)

invariant valueInserted(uint256 i) 
    i < getLength() => isListed(getWithDefaultValue(i))


invariant uniqueArray(uint256 i, uint256 j)
    i != j => (
        (getWithDefaultValue(i) != getWithDefaultValue(j)) || 
		(getWithDefaultValue(i) == 0)
	)
	{
		preserved {
			requireInvariant valueInserted(i);
			requireInvariant valueInserted(j);
		}
	}
