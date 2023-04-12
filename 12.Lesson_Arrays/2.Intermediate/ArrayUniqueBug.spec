methods {
    set(uint, address)                              envfree
    push(address)                                   envfree
    pop()                                           envfree
    removeReplaceFromEnd(uint)                      envfree
    get(uint)                   returns (address)   envfree
    getWithDefaultValue(uint)   returns (address)   envfree
    getArr()                    returns (address[]) envfree
    getLength()                 returns (uint)      envfree
    frequency(address)          returns (uint)      envfree
}

invariant addressFrequency(address a)
    a != 0 => frequency(a) <= 1

// invariant noElementsInForbiddenPositions(uint256 i)
//  i >= getLength() => getWithDefaultValue(i)


invariant uniqueArray(uint256 i, uint256 j) 
    i != j => (
        (getWithDefaultValue(i) != getWithDefaultValue(j)) ||
		((getWithDefaultValue(i) == 0) && (getWithDefaultValue(j) == 0))
	)
    {
        preserved {
            requireInvariant addressFrequency(getWithDefaultValue(i));
            requireInvariant addressFrequency(getWithDefaultValue(j));
        }
    }
