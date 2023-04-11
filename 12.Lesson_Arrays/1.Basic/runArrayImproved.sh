certoraRun ArrayImproved.sol:Array \
--verify Array:ArrayImproved.spec \
--send_only \
--optimistic_loop \
--loop_iter 4 \
--rule_sanity \
--msg "Array.sol with sanity check"

# --solc solc8.6 \
