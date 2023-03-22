
methods {
	ballAt() returns uint256 envfree
	pass() envfree
}

//invariant neverReachPlayer4()
//	ballAt() != 4
//	{
//		preserved with(env e) {
//			require ballAt() != 3;
//		}
//	}


rule neverReachPlayer4AsRule(method f) {
	calldataarg args;
	env e;

	require ballAt() != 4 && ballAt() != 3;
	f(e, args);
	assert ballAt() != 4;
}
