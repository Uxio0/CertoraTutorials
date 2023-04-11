// #contract Array.sol:Array
methods {
    get(uint) returns (address) envfree
    getWithDefaultValue(uint) returns (address) envfree
    getLength() returns (uint) envfree
}


invariant uniqueArrayUsingRevert(uint256 i, uint256 j)
(
    (getWithDefaultValue(i) == getWithDefaultValue(j)) => (i == j) || (getWithDefaultValue(i) == 0)
)


invariant uniqueArray(uint256 i, uint256 j)
    i != j => ((get(i) != get(j)) || ((get(i) == 0) && (get(j) == 0)))
