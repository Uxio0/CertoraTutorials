certoraRun ReserveListFixed.sol:ReserveList --verify ReserveList:Reserve.spec \
--optimistic_loop \
--loop_iter 3 \
--msg "correlated lists broken"

# --solc solc8.7 \

# --optimistic_loop and --loop_iter 3 are flags that handle loops.
# They are needed here, but don't mind them, you will learn about loop handling in a future lesson.
