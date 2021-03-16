import math

ang = float(input('Digite o angulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno do angulo {:.2f} é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(ang, sen, cos, tan))


