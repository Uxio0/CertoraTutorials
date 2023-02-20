(declare-const circle Int)
(declare-const square Int)
(declare-const triangle Int)

(assert (= (+ circle circle) 10))
(assert (= (+ (* circle square) square) 12))
(assert (= (- (* circle square) (* triangle circle)) circle))
(check-sat)
(get-model)

; Circle = 1
; Square = 2
; Triangle = 1
