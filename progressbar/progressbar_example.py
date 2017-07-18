#!/usr/bin/python
# coding:utf-8
import sys
import time
from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer
 
examples = []
 
def example(fn):
    try:
        name = 'Example %d' % int(fn.__name__[7:])
    except:
        name = fn.__name__
 
    def wrapped():
        try:
            sys.stdout.write('Running: %s\n' % name)
            fn()
            sys.stdout.write('\n')
        except KeyboardInterrupt:
            sys.stdout.write('\nSkipping example.\n\n')
 
    examples.append(wrapped)
    return wrapped
 
@example
def example0():
    pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=300).start()
    for i in range(300):
        time.sleep(0.01)
        pbar.update(i + 1)
    pbar.finish()
 
@example
def example1():
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10 * i + 1)
    pbar.finish()
 
@example
def example2():
    class CrazyFileTransferSpeed(FileTransferSpeed):
        """It's bigger between 45 and 80 percent."""
 
        def update(self, pbar):
            if 45 < pbar.percentage() < 80:
                return 'Bigger Now ' + FileTransferSpeed.update(self, pbar)
            else:
                return FileTransferSpeed.update(self, pbar)
 
    widgets = [CrazyFileTransferSpeed(), ' <<<', Bar(), '>>> ',
               Percentage(), ' ', ETA()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000)
    # maybe do something
    pbar.start()
    for i in range(2000000):
        # do something
        pbar.update(5 * i + 1)
    pbar.finish()
 
@example
def example3():
    widgets = [Bar('>'), ' ', ETA(), ' ', ReverseBar('<')]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10 * i + 1)
    pbar.finish()
 
@example
def example4():
    widgets = ['Test: ', Percentage(), ' ',
               Bar(marker='0', left='[', right=']'),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=500)
    pbar.start()
    for i in range(100, 500 + 1, 50):
        time.sleep(0.2)
        pbar.update(i)
    pbar.finish()
 
@example
def example5():
    pbar = ProgressBar(widgets=[SimpleProgress()], maxval=17).start()
    for i in range(17):
        time.sleep(0.2)
        pbar.update(i + 1)
    pbar.finish()
 
@example
def example6():
    pbar = ProgressBar().start()
    for i in range(100):
        time.sleep(0.01)
        pbar.update(i + 1)
    pbar.finish()
 
@example
def example7():
    pbar = ProgressBar()  # Progressbar can guess maxval automatically.
    for i in pbar(range(80)):
        time.sleep(0.01)
 
@example
def example8():
    pbar = ProgressBar(maxval=80)  # Progressbar can't guess maxval.
    for i in pbar((i for i in range(80))):
        time.sleep(0.01)
 
@example
def example9():
    pbar = ProgressBar(widgets=['Working: ', AnimatedMarker()])
    for i in pbar((i for i in range(50))):
        time.sleep(.08)
 
@example
def example10():
    widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(150))):
        time.sleep(0.1)
 
@example
def example11():
    widgets = [FormatLabel('Processed: %(value)d lines (in: %(elapsed)s)')]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(150))):
        time.sleep(0.1)
 
@example
def example12():
    widgets = ['Balloon: ', AnimatedMarker(markers='.oO<a href="http://www.jobbole.com/members/weiboyes8848">@*</a> ')]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(24))):
        time.sleep(0.3)
 
@example
def example13():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Arrows: ', AnimatedMarker(markers='←↖↑↗→↘↓↙')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.3)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
 
@example
def example14():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Arrows: ', AnimatedMarker(markers='◢◣◤◥')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.3)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
 
@example
def example15():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Wheels: ', AnimatedMarker(markers='◐◓◑◒')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.3)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
 
@example
def example16():
    widgets = [FormatLabel('Bouncer: value %(value)d - '), BouncingBar()]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(180))):
        time.sleep(0.05)
 
@example
def example17():
    widgets = [FormatLabel('Animated Bouncer: value %(value)d - '),
               BouncingBar(marker=RotatingMarker())]
 
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(180))):
        time.sleep(0.05)
 
@example
def example18():
    widgets = [Percentage(),
               ' ', Bar(),
               ' ', ETA(),
               ' ', AdaptiveETA()]
    pbar = ProgressBar(widgets=widgets, maxval=500)
    pbar.start()
    for i in range(500):
        time.sleep(0.01 + (i < 100) * 0.01 + (i > 400) * 0.9)
        pbar.update(i + 1)
    pbar.finish()
 
@example
def example19():
    pbar = ProgressBar()
    for i in pbar([]):
        pass
    pbar.finish()

class ProgressBar:
    def __init__(self, count = 0, total = 0, width = 50):
        self.count = count
        self.total = total
        self.width = width
    def move(self):
        self.count += 1
    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        print s
        progress = self.width * self.count / self.total
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-' * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()
 
bar = ProgressBar(total = 10)
for i in range(10):
    bar.move()
    bar.log('We have arrived at: ' + str(i + 1))
    time.sleep(1)

 
try:
    for example in examples:
        example()
except KeyboardInterrupt:
    sys.stdout('\nQuitting examples.\n')

