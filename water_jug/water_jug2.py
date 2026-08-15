def water_jug(jug1cap,jug2cap,target):
    jug1=0
    jug2=0

    while jug1!=target and jug2!=target:
        if jug1==0:
            jug1=jug1cap
            print(f'Pour the jug 1:{({jug1},{jug2})}')
        transfer=min(jug1,jug2cap-jug2)
        jug1-=transfer
        jug2+=transfer
        print(f'After transfering from jug1 to jug2:{({jug1},{jug2})}')
        if jug1==target or jug2==target:
            break
        if jug2==jug2cap:
            jug2=0
        print(f"clearing water from jug 2{({jug1},{jug2})}")

    print('goal reached')
    print(f"The final target is :{({jug1},{jug2})}")


water_jug(8,3,7)



   
