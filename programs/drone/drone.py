class DroneStatus(object):
    def __init__(self, text):  # 获取日志
        self.log = []  # 日志列表
        self.count = 0  # 存储日志条数
        self.status = True  # 判断是否故障
        try:
            with open(text, 'r') as file:  # 获取日志
                for line in file.readlines():
                    if len(line.strip()) == 18:  # 当日志包含偏移坐标
                        drone_id, x, y, z, offset_x, offset_y, offset_z = line.strip().split(' ', 6)
                        log_by_line = {}
                        log_by_line['id'] = drone_id
                        log_by_line['x'] = eval(x)
                        log_by_line['y'] = eval(y)
                        log_by_line['z'] = eval(z)
                        log_by_line['offset_x'] = eval(offset_x)
                        log_by_line['offset_y'] = eval(offset_y)
                        log_by_line['offset_z'] = eval(offset_z)
                    elif len(line.strip()) == 12:  # 当日志不包含偏移坐标
                        drone_id, x, y, z = line.strip().split(' ', 3)
                        log_by_line = {}
                        log_by_line['id'] = drone_id
                        log_by_line['x'] = eval(x)
                        log_by_line['y'] = eval(y)
                        log_by_line['z'] = eval(z)
                        log_by_line['offset_x'] = 0
                        log_by_line['offset_y'] = 0
                        log_by_line['offset_z'] = 0
                    else:
                        print("log fault")  # 日志错误
                    self.count += 1
                    self.log.append(log_by_line)
        except Exception as exception:
            print(str(exception))

    def get_status(self, index):  # 获取无人机状态
        if index > self.count - 1:  # 指定消息不存在
            return print("Cannot find " + str(index))
        if not self.status:  # 无人机曾故障
            return print("Error: " + str(index))
        if isinstance(self.log[index]['x'], int) \
                and isinstance(self.log[index]['y'], int) \
                and isinstance(self.log[index]['z'], int):  # 判断是x, y, z否为整数
            if index == 0:  # 无人机初始坐标
                x = self.log[index]['x'] + self.log[index]['offset_x']
                y = self.log[index]['y'] + self.log[index]['offset_y']
                z = self.log[index]['z'] + self.log[index]['offset_z']
                return print(self.log[index]['id']
                             + ' ' + str(index)
                             + ' ' + str(x) + ' ' + str(y) + ' ' + str(z))

            elif self.log[index]['x'] == self.log[index - 1]['x'] + self.log[index - 1]['offset_x'] \
                    and self.log[index]['y'] == \
                    self.log[index - 1]['y'] + self.log[index - 1]['offset_y'] \
                    and self.log[index]['z'] == \
                    self.log[index - 1]['z'] + self.log[index - 1]['offset_z']:  # 判断当前坐标是否为前坐标与偏移之和
                x = self.log[index]['x'] + self.log[index]['offset_x']
                y = self.log[index]['y'] + self.log[index]['offset_y']
                z = self.log[index]['z'] + self.log[index]['offset_z']
                return print(self.log[index]['id']
                             + ' ' + str(index)
                             + ' ' + str(x) + ' ' + str(y) + ' ' + str(z))
            else:  # 无人机故障
                self.status = False
                return print("Error: " + str(index))
        else:
            print("Wrong input:" + str(index))  # 错误数据类型：x, y, z不全为整型


def main():
    text = 'signal_log.txt'  # 日志目录
    log = DroneStatus(text)  # 消息序号
    for i in range(7):
        log.get_status(i)


if __name__ == "__main__":
    main()
