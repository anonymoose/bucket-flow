from datetime import datetime


def days_between(d1, d2):
    d, m, y = d1.split('/')
    d1 = datetime.strptime('%s/%s/%s' % (d.zfill(2), m.zfill(2), y), "%m/%d/%Y")
    d, m, y = d2.split('/')
    d2 = datetime.strptime('%s/%s/%s' % (d.zfill(2), m.zfill(2), y), "%m/%d/%Y")
    return abs((d2 - d1).days)


def main(lines):
    inv = {}
    for l in [l.strip() for l in lines]:
        (flavor, start, end) = l.split(',')
        diff = days_between(start, end)
        if flavor not in inv:
            inv[flavor] = {
                'cnt': 1,
                'diff_sum': diff,
                'max_diff': diff,
                'min_diff': diff
            }
        else:
            inv[flavor]['cnt'] += 1
            inv[flavor]['diff_sum'] += diff
            inv[flavor]['max_diff'] = max(inv[flavor]['max_diff'], diff)
            inv[flavor]['min_diff'] = min(inv[flavor]['min_diff'], diff)

    for flavor in inv:
        dat = inv[flavor]
        diff_sum = dat['diff_sum']
        cnt = dat['cnt']
        max_diff = dat['max_diff']
        min_diff = dat['min_diff']
        avg = round(float(diff_sum / cnt), 1)
        print('{:<20},{:<20},{:>10},{:>13},{:>13}'.format(cnt, flavor, avg, max_diff, min_diff))


if __name__ == '__main__':
    with open('inventory.csv') as f:
        lines = f.readlines()
    main(lines)
