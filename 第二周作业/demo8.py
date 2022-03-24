from turtle import*
fillcolor("yellow")
begin_fill()
while True:
    forward(200)
    left(170)   
    if abs(pos())<1:
        break
end_fill()
done()
# done()界面停留