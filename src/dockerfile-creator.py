import sys

if len(sys.argv) == 2:
    print('dockerfile-creator Missing parameter')
    sys.exit()

env = sys.argv[1]
service = sys.argv[2]

print('dockerfile-creator run')
print('dockerfile-creator param - env: {}, service: {}'.format(env, service))

file = open('../data/Dockerfile', 'r')
fileData = file.read()
file.close()

fileData = fileData.replace('#{ENV}', env).replace('#{SERVICE}', service)

file = open('../out/Dockerfile', 'w')
file.write(fileData)
file.close()
print('dockerfile-creator complete')

# python3 dockerfile-creator.py "A" "B"