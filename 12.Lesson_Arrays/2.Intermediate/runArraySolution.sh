certoraRun ArraySolution.sol \
--verify ArraySolution:ArrayUniqueBug.spec \
--send_only \
--optimistic_loop \
--loop_iter 4 \
--rule_sanity \
--msg "ArraySolution.sol with sanity check"

# --solc solc8.6 \