def run(r):
    if r in ['0', '2', '4', '6']:
        strike[batsmen[0]] += int(r)
    if r in ['1', '3', '5']:
        strike[batsmen[0]] += int(r)
        batsmen[0], batsmen[1] = batsmen[1], batsmen[0]
    if r in ['W', 'N']:
        strike[batsmen[0]] += 0
    if r == 'O':
        batsmen[0], batsmen[2] = batsmen[2], batsmen[0]


batsmen = ['b1', 'b2', 'b3']
strike = {'b1': 0, 'b2': 0, 'b3': 0}
balls = input().split()
O = balls.count('O')
for i in range(len(balls)):
    run(balls[i])
print(strike['b1'])
print(strike['b2'])
print(strike['b3'])