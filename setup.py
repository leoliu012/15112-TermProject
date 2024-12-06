# code below is learned from ChatGPT and
# https://www.reddit.com/r/learnpython/comments/afjoup/making_python_code_into_an_executable_app_on_mac/

from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    ('assets/backgrounds', ['assets/backgrounds/intro.jpg']),
    ('assets/button', [
        'assets/button/button1.png',
        'assets/button/diffSel.png',
        'assets/button/plus.png',
        'assets/button/minus.png',
        'assets/button/diffSel.png'
    ]),
('', ['savedInfo.txt']),
    ('assets/cars', [
        'assets/cars/0.png',
        'assets/cars/1.png',
        'assets/cars/2.png',
    ]),
    ('assets/control', [
        'assets/control/bar.png',
        'assets/control/bar1.png',
    ]),
    ('assets/instructions/straightRoad', ['./assets/instructions/straightRoad/ezgif-frame-001.jpg', './assets/instructions/straightRoad/ezgif-frame-002.jpg', './assets/instructions/straightRoad/ezgif-frame-003.jpg', './assets/instructions/straightRoad/ezgif-frame-004.jpg', './assets/instructions/straightRoad/ezgif-frame-005.jpg', './assets/instructions/straightRoad/ezgif-frame-006.jpg', './assets/instructions/straightRoad/ezgif-frame-007.jpg', './assets/instructions/straightRoad/ezgif-frame-008.jpg', './assets/instructions/straightRoad/ezgif-frame-009.jpg', './assets/instructions/straightRoad/ezgif-frame-010.jpg', './assets/instructions/straightRoad/ezgif-frame-011.jpg', './assets/instructions/straightRoad/ezgif-frame-012.jpg', './assets/instructions/straightRoad/ezgif-frame-013.jpg', './assets/instructions/straightRoad/ezgif-frame-014.jpg', './assets/instructions/straightRoad/ezgif-frame-015.jpg', './assets/instructions/straightRoad/ezgif-frame-016.jpg', './assets/instructions/straightRoad/ezgif-frame-017.jpg', './assets/instructions/straightRoad/ezgif-frame-018.jpg', './assets/instructions/straightRoad/ezgif-frame-019.jpg', './assets/instructions/straightRoad/ezgif-frame-020.jpg', './assets/instructions/straightRoad/ezgif-frame-021.jpg', './assets/instructions/straightRoad/ezgif-frame-022.jpg', './assets/instructions/straightRoad/ezgif-frame-023.jpg', './assets/instructions/straightRoad/ezgif-frame-024.jpg', './assets/instructions/straightRoad/ezgif-frame-025.jpg', './assets/instructions/straightRoad/ezgif-frame-026.jpg', './assets/instructions/straightRoad/ezgif-frame-027.jpg', './assets/instructions/straightRoad/ezgif-frame-028.jpg', './assets/instructions/straightRoad/ezgif-frame-029.jpg', './assets/instructions/straightRoad/ezgif-frame-030.jpg', './assets/instructions/straightRoad/ezgif-frame-031.jpg', './assets/instructions/straightRoad/ezgif-frame-032.jpg', './assets/instructions/straightRoad/ezgif-frame-033.jpg', './assets/instructions/straightRoad/ezgif-frame-034.jpg', './assets/instructions/straightRoad/ezgif-frame-035.jpg', './assets/instructions/straightRoad/ezgif-frame-036.jpg', './assets/instructions/straightRoad/ezgif-frame-037.jpg', './assets/instructions/straightRoad/ezgif-frame-038.jpg', './assets/instructions/straightRoad/ezgif-frame-039.jpg', './assets/instructions/straightRoad/ezgif-frame-040.jpg', './assets/instructions/straightRoad/ezgif-frame-041.jpg', './assets/instructions/straightRoad/ezgif-frame-042.jpg', './assets/instructions/straightRoad/ezgif-frame-043.jpg', './assets/instructions/straightRoad/ezgif-frame-044.jpg', './assets/instructions/straightRoad/ezgif-frame-045.jpg', './assets/instructions/straightRoad/ezgif-frame-046.jpg', './assets/instructions/straightRoad/ezgif-frame-047.jpg', './assets/instructions/straightRoad/ezgif-frame-048.jpg', './assets/instructions/straightRoad/ezgif-frame-049.jpg', './assets/instructions/straightRoad/ezgif-frame-050.jpg', './assets/instructions/straightRoad/ezgif-frame-051.jpg', './assets/instructions/straightRoad/ezgif-frame-052.jpg', './assets/instructions/straightRoad/ezgif-frame-053.jpg', './assets/instructions/straightRoad/ezgif-frame-054.jpg', './assets/instructions/straightRoad/ezgif-frame-055.jpg', './assets/instructions/straightRoad/ezgif-frame-056.jpg', './assets/instructions/straightRoad/ezgif-frame-057.jpg', './assets/instructions/straightRoad/ezgif-frame-058.jpg', './assets/instructions/straightRoad/ezgif-frame-059.jpg', './assets/instructions/straightRoad/ezgif-frame-060.jpg', './assets/instructions/straightRoad/ezgif-frame-061.jpg', './assets/instructions/straightRoad/ezgif-frame-062.jpg', './assets/instructions/straightRoad/ezgif-frame-063.jpg', './assets/instructions/straightRoad/ezgif-frame-064.jpg', './assets/instructions/straightRoad/ezgif-frame-065.jpg', './assets/instructions/straightRoad/ezgif-frame-066.jpg', './assets/instructions/straightRoad/ezgif-frame-067.jpg', './assets/instructions/straightRoad/ezgif-frame-068.jpg', './assets/instructions/straightRoad/ezgif-frame-069.jpg', './assets/instructions/straightRoad/ezgif-frame-070.jpg', './assets/instructions/straightRoad/ezgif-frame-071.jpg', './assets/instructions/straightRoad/ezgif-frame-072.jpg', './assets/instructions/straightRoad/ezgif-frame-073.jpg', './assets/instructions/straightRoad/ezgif-frame-074.jpg', './assets/instructions/straightRoad/ezgif-frame-075.jpg', './assets/instructions/straightRoad/ezgif-frame-076.jpg', './assets/instructions/straightRoad/ezgif-frame-077.jpg', './assets/instructions/straightRoad/ezgif-frame-078.jpg', './assets/instructions/straightRoad/ezgif-frame-079.jpg', './assets/instructions/straightRoad/ezgif-frame-080.jpg', './assets/instructions/straightRoad/ezgif-frame-081.jpg', './assets/instructions/straightRoad/ezgif-frame-082.jpg', './assets/instructions/straightRoad/ezgif-frame-083.jpg', './assets/instructions/straightRoad/ezgif-frame-084.jpg', './assets/instructions/straightRoad/ezgif-frame-085.jpg', './assets/instructions/straightRoad/ezgif-frame-086.jpg', './assets/instructions/straightRoad/ezgif-frame-087.jpg', './assets/instructions/straightRoad/ezgif-frame-088.jpg', './assets/instructions/straightRoad/ezgif-frame-089.jpg', './assets/instructions/straightRoad/ezgif-frame-090.jpg', './assets/instructions/straightRoad/ezgif-frame-091.jpg', './assets/instructions/straightRoad/ezgif-frame-092.jpg', './assets/instructions/straightRoad/ezgif-frame-093.jpg', './assets/instructions/straightRoad/ezgif-frame-094.jpg', './assets/instructions/straightRoad/ezgif-frame-095.jpg', './assets/instructions/straightRoad/ezgif-frame-096.jpg', './assets/instructions/straightRoad/ezgif-frame-097.jpg', './assets/instructions/straightRoad/ezgif-frame-098.jpg', './assets/instructions/straightRoad/ezgif-frame-099.jpg', './assets/instructions/straightRoad/ezgif-frame-100.jpg', './assets/instructions/straightRoad/ezgif-frame-101.jpg', './assets/instructions/straightRoad/ezgif-frame-102.jpg', './assets/instructions/straightRoad/ezgif-frame-103.jpg', './assets/instructions/straightRoad/ezgif-frame-104.jpg', './assets/instructions/straightRoad/ezgif-frame-105.jpg', './assets/instructions/straightRoad/ezgif-frame-106.jpg', './assets/instructions/straightRoad/ezgif-frame-107.jpg', './assets/instructions/straightRoad/ezgif-frame-108.jpg', './assets/instructions/straightRoad/ezgif-frame-109.jpg', './assets/instructions/straightRoad/ezgif-frame-110.jpg']),
    ('assets/instructions/bridge', ['./assets/instructions/bridge/ezgif-frame-001.jpg', './assets/instructions/bridge/ezgif-frame-002.jpg', './assets/instructions/bridge/ezgif-frame-003.jpg', './assets/instructions/bridge/ezgif-frame-004.jpg', './assets/instructions/bridge/ezgif-frame-005.jpg', './assets/instructions/bridge/ezgif-frame-006.jpg', './assets/instructions/bridge/ezgif-frame-007.jpg', './assets/instructions/bridge/ezgif-frame-008.jpg', './assets/instructions/bridge/ezgif-frame-009.jpg', './assets/instructions/bridge/ezgif-frame-010.jpg', './assets/instructions/bridge/ezgif-frame-011.jpg', './assets/instructions/bridge/ezgif-frame-012.jpg', './assets/instructions/bridge/ezgif-frame-013.jpg', './assets/instructions/bridge/ezgif-frame-014.jpg', './assets/instructions/bridge/ezgif-frame-015.jpg', './assets/instructions/bridge/ezgif-frame-016.jpg', './assets/instructions/bridge/ezgif-frame-017.jpg', './assets/instructions/bridge/ezgif-frame-018.jpg', './assets/instructions/bridge/ezgif-frame-019.jpg', './assets/instructions/bridge/ezgif-frame-020.jpg', './assets/instructions/bridge/ezgif-frame-021.jpg', './assets/instructions/bridge/ezgif-frame-022.jpg', './assets/instructions/bridge/ezgif-frame-023.jpg', './assets/instructions/bridge/ezgif-frame-024.jpg', './assets/instructions/bridge/ezgif-frame-025.jpg', './assets/instructions/bridge/ezgif-frame-026.jpg', './assets/instructions/bridge/ezgif-frame-027.jpg', './assets/instructions/bridge/ezgif-frame-028.jpg', './assets/instructions/bridge/ezgif-frame-029.jpg', './assets/instructions/bridge/ezgif-frame-030.jpg', './assets/instructions/bridge/ezgif-frame-031.jpg', './assets/instructions/bridge/ezgif-frame-032.jpg', './assets/instructions/bridge/ezgif-frame-033.jpg', './assets/instructions/bridge/ezgif-frame-034.jpg', './assets/instructions/bridge/ezgif-frame-035.jpg', './assets/instructions/bridge/ezgif-frame-036.jpg', './assets/instructions/bridge/ezgif-frame-037.jpg', './assets/instructions/bridge/ezgif-frame-038.jpg', './assets/instructions/bridge/ezgif-frame-039.jpg', './assets/instructions/bridge/ezgif-frame-040.jpg', './assets/instructions/bridge/ezgif-frame-041.jpg', './assets/instructions/bridge/ezgif-frame-042.jpg', './assets/instructions/bridge/ezgif-frame-043.jpg', './assets/instructions/bridge/ezgif-frame-044.jpg', './assets/instructions/bridge/ezgif-frame-045.jpg', './assets/instructions/bridge/ezgif-frame-046.jpg', './assets/instructions/bridge/ezgif-frame-047.jpg', './assets/instructions/bridge/ezgif-frame-048.jpg', './assets/instructions/bridge/ezgif-frame-049.jpg', './assets/instructions/bridge/ezgif-frame-050.jpg', './assets/instructions/bridge/ezgif-frame-051.jpg', './assets/instructions/bridge/ezgif-frame-052.jpg', './assets/instructions/bridge/ezgif-frame-053.jpg', './assets/instructions/bridge/ezgif-frame-054.jpg', './assets/instructions/bridge/ezgif-frame-055.jpg', './assets/instructions/bridge/ezgif-frame-056.jpg', './assets/instructions/bridge/ezgif-frame-057.jpg', './assets/instructions/bridge/ezgif-frame-058.jpg', './assets/instructions/bridge/ezgif-frame-059.jpg', './assets/instructions/bridge/ezgif-frame-060.jpg', './assets/instructions/bridge/ezgif-frame-061.jpg', './assets/instructions/bridge/ezgif-frame-062.jpg', './assets/instructions/bridge/ezgif-frame-063.jpg', './assets/instructions/bridge/ezgif-frame-064.jpg', './assets/instructions/bridge/ezgif-frame-065.jpg', './assets/instructions/bridge/ezgif-frame-066.jpg', './assets/instructions/bridge/ezgif-frame-067.jpg', './assets/instructions/bridge/ezgif-frame-068.jpg', './assets/instructions/bridge/ezgif-frame-069.jpg', './assets/instructions/bridge/ezgif-frame-070.jpg', './assets/instructions/bridge/ezgif-frame-071.jpg', './assets/instructions/bridge/ezgif-frame-072.jpg', './assets/instructions/bridge/ezgif-frame-073.jpg', './assets/instructions/bridge/ezgif-frame-074.jpg', './assets/instructions/bridge/ezgif-frame-075.jpg', './assets/instructions/bridge/ezgif-frame-076.jpg', './assets/instructions/bridge/ezgif-frame-077.jpg', './assets/instructions/bridge/ezgif-frame-078.jpg', './assets/instructions/bridge/ezgif-frame-079.jpg', './assets/instructions/bridge/ezgif-frame-080.jpg', './assets/instructions/bridge/ezgif-frame-081.jpg', './assets/instructions/bridge/ezgif-frame-082.jpg', './assets/instructions/bridge/ezgif-frame-083.jpg', './assets/instructions/bridge/ezgif-frame-084.jpg', './assets/instructions/bridge/ezgif-frame-085.jpg', './assets/instructions/bridge/ezgif-frame-086.jpg', './assets/instructions/bridge/ezgif-frame-087.jpg', './assets/instructions/bridge/ezgif-frame-088.jpg', './assets/instructions/bridge/ezgif-frame-089.jpg', './assets/instructions/bridge/ezgif-frame-090.jpg', './assets/instructions/bridge/ezgif-frame-091.jpg', './assets/instructions/bridge/ezgif-frame-092.jpg', './assets/instructions/bridge/ezgif-frame-093.jpg', './assets/instructions/bridge/ezgif-frame-094.jpg', './assets/instructions/bridge/ezgif-frame-095.jpg', './assets/instructions/bridge/ezgif-frame-096.jpg', './assets/instructions/bridge/ezgif-frame-097.jpg', './assets/instructions/bridge/ezgif-frame-098.jpg', './assets/instructions/bridge/ezgif-frame-099.jpg', './assets/instructions/bridge/ezgif-frame-100.jpg', './assets/instructions/bridge/ezgif-frame-101.jpg', './assets/instructions/bridge/ezgif-frame-102.jpg', './assets/instructions/bridge/ezgif-frame-103.jpg', './assets/instructions/bridge/ezgif-frame-104.jpg', './assets/instructions/bridge/ezgif-frame-105.jpg', './assets/instructions/bridge/ezgif-frame-106.jpg', './assets/instructions/bridge/ezgif-frame-107.jpg', './assets/instructions/bridge/ezgif-frame-108.jpg', './assets/instructions/bridge/ezgif-frame-109.jpg', './assets/instructions/bridge/ezgif-frame-110.jpg', './assets/instructions/bridge/ezgif-frame-111.jpg', './assets/instructions/bridge/ezgif-frame-112.jpg', './assets/instructions/bridge/ezgif-frame-113.jpg', './assets/instructions/bridge/ezgif-frame-114.jpg', './assets/instructions/bridge/ezgif-frame-115.jpg', './assets/instructions/bridge/ezgif-frame-116.jpg', './assets/instructions/bridge/ezgif-frame-117.jpg', './assets/instructions/bridge/ezgif-frame-118.jpg', './assets/instructions/bridge/ezgif-frame-119.jpg', './assets/instructions/bridge/ezgif-frame-120.jpg', './assets/instructions/bridge/ezgif-frame-121.jpg', './assets/instructions/bridge/ezgif-frame-122.jpg', './assets/instructions/bridge/ezgif-frame-123.jpg', './assets/instructions/bridge/ezgif-frame-124.jpg', './assets/instructions/bridge/ezgif-frame-125.jpg', './assets/instructions/bridge/ezgif-frame-126.jpg', './assets/instructions/bridge/ezgif-frame-127.jpg', './assets/instructions/bridge/ezgif-frame-128.jpg', './assets/instructions/bridge/ezgif-frame-129.jpg', './assets/instructions/bridge/ezgif-frame-130.jpg', './assets/instructions/bridge/ezgif-frame-131.jpg', './assets/instructions/bridge/ezgif-frame-132.jpg', './assets/instructions/bridge/ezgif-frame-133.jpg', './assets/instructions/bridge/ezgif-frame-134.jpg', './assets/instructions/bridge/ezgif-frame-135.jpg', './assets/instructions/bridge/ezgif-frame-136.jpg', './assets/instructions/bridge/ezgif-frame-137.jpg', './assets/instructions/bridge/ezgif-frame-138.jpg', './assets/instructions/bridge/ezgif-frame-139.jpg', './assets/instructions/bridge/ezgif-frame-140.jpg', './assets/instructions/bridge/ezgif-frame-141.jpg', './assets/instructions/bridge/ezgif-frame-142.jpg', './assets/instructions/bridge/ezgif-frame-143.jpg', './assets/instructions/bridge/ezgif-frame-144.jpg', './assets/instructions/bridge/ezgif-frame-145.jpg', './assets/instructions/bridge/ezgif-frame-146.jpg', './assets/instructions/bridge/ezgif-frame-147.jpg', './assets/instructions/bridge/ezgif-frame-148.jpg', './assets/instructions/bridge/ezgif-frame-149.jpg', './assets/instructions/bridge/ezgif-frame-150.jpg', './assets/instructions/bridge/ezgif-frame-151.jpg', './assets/instructions/bridge/ezgif-frame-152.jpg', './assets/instructions/bridge/ezgif-frame-153.jpg', './assets/instructions/bridge/ezgif-frame-154.jpg', './assets/instructions/bridge/ezgif-frame-155.jpg', './assets/instructions/bridge/ezgif-frame-156.jpg', './assets/instructions/bridge/ezgif-frame-157.jpg', './assets/instructions/bridge/ezgif-frame-158.jpg', './assets/instructions/bridge/ezgif-frame-159.jpg', './assets/instructions/bridge/ezgif-frame-160.jpg', './assets/instructions/bridge/ezgif-frame-161.jpg', './assets/instructions/bridge/ezgif-frame-162.jpg', './assets/instructions/bridge/ezgif-frame-163.jpg', './assets/instructions/bridge/ezgif-frame-164.jpg', './assets/instructions/bridge/ezgif-frame-165.jpg', './assets/instructions/bridge/ezgif-frame-166.jpg', './assets/instructions/bridge/ezgif-frame-167.jpg', './assets/instructions/bridge/ezgif-frame-168.jpg', './assets/instructions/bridge/ezgif-frame-169.jpg', './assets/instructions/bridge/ezgif-frame-170.jpg', './assets/instructions/bridge/ezgif-frame-171.jpg', './assets/instructions/bridge/ezgif-frame-172.jpg', './assets/instructions/bridge/ezgif-frame-173.jpg', './assets/instructions/bridge/ezgif-frame-174.jpg', './assets/instructions/bridge/ezgif-frame-175.jpg', './assets/instructions/bridge/ezgif-frame-176.jpg', './assets/instructions/bridge/ezgif-frame-177.jpg', './assets/instructions/bridge/ezgif-frame-178.jpg', './assets/instructions/bridge/ezgif-frame-179.jpg', './assets/instructions/bridge/ezgif-frame-180.jpg', './assets/instructions/bridge/ezgif-frame-181.jpg', './assets/instructions/bridge/ezgif-frame-182.jpg', './assets/instructions/bridge/ezgif-frame-183.jpg', './assets/instructions/bridge/ezgif-frame-184.jpg', './assets/instructions/bridge/ezgif-frame-185.jpg', './assets/instructions/bridge/ezgif-frame-186.jpg', './assets/instructions/bridge/ezgif-frame-187.jpg', './assets/instructions/bridge/ezgif-frame-188.jpg', './assets/instructions/bridge/ezgif-frame-189.jpg', './assets/instructions/bridge/ezgif-frame-190.jpg', './assets/instructions/bridge/ezgif-frame-191.jpg', './assets/instructions/bridge/ezgif-frame-192.jpg', './assets/instructions/bridge/ezgif-frame-193.jpg', './assets/instructions/bridge/ezgif-frame-194.jpg', './assets/instructions/bridge/ezgif-frame-195.jpg', './assets/instructions/bridge/ezgif-frame-196.jpg', './assets/instructions/bridge/ezgif-frame-197.jpg', './assets/instructions/bridge/ezgif-frame-198.jpg', './assets/instructions/bridge/ezgif-frame-199.jpg', './assets/instructions/bridge/ezgif-frame-200.jpg']),
    ('assets/instructions/curvedRoad', ['./assets/instructions/curvedRoad/ezgif-frame-001.jpg', './assets/instructions/curvedRoad/ezgif-frame-002.jpg', './assets/instructions/curvedRoad/ezgif-frame-003.jpg', './assets/instructions/curvedRoad/ezgif-frame-004.jpg', './assets/instructions/curvedRoad/ezgif-frame-005.jpg', './assets/instructions/curvedRoad/ezgif-frame-006.jpg', './assets/instructions/curvedRoad/ezgif-frame-007.jpg', './assets/instructions/curvedRoad/ezgif-frame-008.jpg', './assets/instructions/curvedRoad/ezgif-frame-009.jpg', './assets/instructions/curvedRoad/ezgif-frame-010.jpg', './assets/instructions/curvedRoad/ezgif-frame-011.jpg', './assets/instructions/curvedRoad/ezgif-frame-012.jpg', './assets/instructions/curvedRoad/ezgif-frame-013.jpg', './assets/instructions/curvedRoad/ezgif-frame-014.jpg', './assets/instructions/curvedRoad/ezgif-frame-015.jpg', './assets/instructions/curvedRoad/ezgif-frame-016.jpg', './assets/instructions/curvedRoad/ezgif-frame-017.jpg', './assets/instructions/curvedRoad/ezgif-frame-018.jpg', './assets/instructions/curvedRoad/ezgif-frame-019.jpg', './assets/instructions/curvedRoad/ezgif-frame-020.jpg', './assets/instructions/curvedRoad/ezgif-frame-021.jpg', './assets/instructions/curvedRoad/ezgif-frame-022.jpg', './assets/instructions/curvedRoad/ezgif-frame-023.jpg', './assets/instructions/curvedRoad/ezgif-frame-024.jpg', './assets/instructions/curvedRoad/ezgif-frame-025.jpg', './assets/instructions/curvedRoad/ezgif-frame-026.jpg', './assets/instructions/curvedRoad/ezgif-frame-027.jpg', './assets/instructions/curvedRoad/ezgif-frame-028.jpg', './assets/instructions/curvedRoad/ezgif-frame-029.jpg', './assets/instructions/curvedRoad/ezgif-frame-030.jpg', './assets/instructions/curvedRoad/ezgif-frame-031.jpg', './assets/instructions/curvedRoad/ezgif-frame-032.jpg', './assets/instructions/curvedRoad/ezgif-frame-033.jpg', './assets/instructions/curvedRoad/ezgif-frame-034.jpg', './assets/instructions/curvedRoad/ezgif-frame-035.jpg', './assets/instructions/curvedRoad/ezgif-frame-036.jpg', './assets/instructions/curvedRoad/ezgif-frame-037.jpg', './assets/instructions/curvedRoad/ezgif-frame-038.jpg', './assets/instructions/curvedRoad/ezgif-frame-039.jpg', './assets/instructions/curvedRoad/ezgif-frame-040.jpg', './assets/instructions/curvedRoad/ezgif-frame-041.jpg', './assets/instructions/curvedRoad/ezgif-frame-042.jpg', './assets/instructions/curvedRoad/ezgif-frame-043.jpg', './assets/instructions/curvedRoad/ezgif-frame-044.jpg', './assets/instructions/curvedRoad/ezgif-frame-045.jpg', './assets/instructions/curvedRoad/ezgif-frame-100.jpg', './assets/instructions/curvedRoad/ezgif-frame-101.jpg', './assets/instructions/curvedRoad/ezgif-frame-102.jpg', './assets/instructions/curvedRoad/ezgif-frame-103.jpg', './assets/instructions/curvedRoad/ezgif-frame-104.jpg', './assets/instructions/curvedRoad/ezgif-frame-105.jpg', './assets/instructions/curvedRoad/ezgif-frame-106.jpg', './assets/instructions/curvedRoad/ezgif-frame-107.jpg', './assets/instructions/curvedRoad/ezgif-frame-108.jpg', './assets/instructions/curvedRoad/ezgif-frame-109.jpg', './assets/instructions/curvedRoad/ezgif-frame-110.jpg', './assets/instructions/curvedRoad/ezgif-frame-111.jpg', './assets/instructions/curvedRoad/ezgif-frame-112.jpg', './assets/instructions/curvedRoad/ezgif-frame-113.jpg', './assets/instructions/curvedRoad/ezgif-frame-114.jpg', './assets/instructions/curvedRoad/ezgif-frame-115.jpg', './assets/instructions/curvedRoad/ezgif-frame-116.jpg', './assets/instructions/curvedRoad/ezgif-frame-117.jpg', './assets/instructions/curvedRoad/ezgif-frame-118.jpg', './assets/instructions/curvedRoad/ezgif-frame-119.jpg', './assets/instructions/curvedRoad/ezgif-frame-120.jpg', './assets/instructions/curvedRoad/ezgif-frame-121.jpg', './assets/instructions/curvedRoad/ezgif-frame-122.jpg', './assets/instructions/curvedRoad/ezgif-frame-123.jpg', './assets/instructions/curvedRoad/ezgif-frame-124.jpg', './assets/instructions/curvedRoad/ezgif-frame-125.jpg', './assets/instructions/curvedRoad/ezgif-frame-126.jpg', './assets/instructions/curvedRoad/ezgif-frame-127.jpg', './assets/instructions/curvedRoad/ezgif-frame-128.jpg', './assets/instructions/curvedRoad/ezgif-frame-129.jpg', './assets/instructions/curvedRoad/ezgif-frame-130.jpg', './assets/instructions/curvedRoad/ezgif-frame-131.jpg', './assets/instructions/curvedRoad/ezgif-frame-132.jpg', './assets/instructions/curvedRoad/ezgif-frame-133.jpg', './assets/instructions/curvedRoad/ezgif-frame-134.jpg', './assets/instructions/curvedRoad/ezgif-frame-135.jpg', './assets/instructions/curvedRoad/ezgif-frame-136.jpg', './assets/instructions/curvedRoad/ezgif-frame-137.jpg', './assets/instructions/curvedRoad/ezgif-frame-138.jpg', './assets/instructions/curvedRoad/ezgif-frame-139.jpg', './assets/instructions/curvedRoad/ezgif-frame-140.jpg', './assets/instructions/curvedRoad/ezgif-frame-141.jpg']),
    ('assets/instructions/remove', ['./assets/instructions/remove/ezgif-frame-001.jpg', './assets/instructions/remove/ezgif-frame-002.jpg', './assets/instructions/remove/ezgif-frame-003.jpg', './assets/instructions/remove/ezgif-frame-004.jpg', './assets/instructions/remove/ezgif-frame-005.jpg', './assets/instructions/remove/ezgif-frame-006.jpg', './assets/instructions/remove/ezgif-frame-007.jpg', './assets/instructions/remove/ezgif-frame-008.jpg', './assets/instructions/remove/ezgif-frame-009.jpg', './assets/instructions/remove/ezgif-frame-010.jpg', './assets/instructions/remove/ezgif-frame-011.jpg', './assets/instructions/remove/ezgif-frame-012.jpg', './assets/instructions/remove/ezgif-frame-013.jpg', './assets/instructions/remove/ezgif-frame-014.jpg', './assets/instructions/remove/ezgif-frame-015.jpg', './assets/instructions/remove/ezgif-frame-016.jpg', './assets/instructions/remove/ezgif-frame-017.jpg', './assets/instructions/remove/ezgif-frame-018.jpg', './assets/instructions/remove/ezgif-frame-019.jpg', './assets/instructions/remove/ezgif-frame-020.jpg', './assets/instructions/remove/ezgif-frame-021.jpg', './assets/instructions/remove/ezgif-frame-022.jpg', './assets/instructions/remove/ezgif-frame-023.jpg', './assets/instructions/remove/ezgif-frame-024.jpg', './assets/instructions/remove/ezgif-frame-025.jpg', './assets/instructions/remove/ezgif-frame-026.jpg', './assets/instructions/remove/ezgif-frame-027.jpg', './assets/instructions/remove/ezgif-frame-028.jpg', './assets/instructions/remove/ezgif-frame-029.jpg', './assets/instructions/remove/ezgif-frame-030.jpg', './assets/instructions/remove/ezgif-frame-031.jpg', './assets/instructions/remove/ezgif-frame-032.jpg', './assets/instructions/remove/ezgif-frame-033.jpg', './assets/instructions/remove/ezgif-frame-034.jpg', './assets/instructions/remove/ezgif-frame-035.jpg', './assets/instructions/remove/ezgif-frame-036.jpg', './assets/instructions/remove/ezgif-frame-037.jpg', './assets/instructions/remove/ezgif-frame-038.jpg', './assets/instructions/remove/ezgif-frame-039.jpg', './assets/instructions/remove/ezgif-frame-040.jpg', './assets/instructions/remove/ezgif-frame-041.jpg', './assets/instructions/remove/ezgif-frame-042.jpg', './assets/instructions/remove/ezgif-frame-043.jpg', './assets/instructions/remove/ezgif-frame-044.jpg', './assets/instructions/remove/ezgif-frame-045.jpg']),
    ('assets/instructions/play', ['./assets/instructions/play/ezgif-frame-001.jpg', './assets/instructions/play/ezgif-frame-002.jpg', './assets/instructions/play/ezgif-frame-003.jpg', './assets/instructions/play/ezgif-frame-004.jpg', './assets/instructions/play/ezgif-frame-005.jpg', './assets/instructions/play/ezgif-frame-006.jpg', './assets/instructions/play/ezgif-frame-007.jpg', './assets/instructions/play/ezgif-frame-008.jpg', './assets/instructions/play/ezgif-frame-009.jpg', './assets/instructions/play/ezgif-frame-010.jpg', './assets/instructions/play/ezgif-frame-011.jpg', './assets/instructions/play/ezgif-frame-012.jpg', './assets/instructions/play/ezgif-frame-013.jpg', './assets/instructions/play/ezgif-frame-014.jpg', './assets/instructions/play/ezgif-frame-015.jpg', './assets/instructions/play/ezgif-frame-016.jpg', './assets/instructions/play/ezgif-frame-017.jpg', './assets/instructions/play/ezgif-frame-018.jpg', './assets/instructions/play/ezgif-frame-019.jpg', './assets/instructions/play/ezgif-frame-020.jpg', './assets/instructions/play/ezgif-frame-021.jpg', './assets/instructions/play/ezgif-frame-022.jpg', './assets/instructions/play/ezgif-frame-023.jpg', './assets/instructions/play/ezgif-frame-024.jpg', './assets/instructions/play/ezgif-frame-025.jpg', './assets/instructions/play/ezgif-frame-026.jpg', './assets/instructions/play/ezgif-frame-027.jpg', './assets/instructions/play/ezgif-frame-028.jpg', './assets/instructions/play/ezgif-frame-029.jpg', './assets/instructions/play/ezgif-frame-030.jpg', './assets/instructions/play/ezgif-frame-031.jpg', './assets/instructions/play/ezgif-frame-032.jpg', './assets/instructions/play/ezgif-frame-033.jpg', './assets/instructions/play/ezgif-frame-034.jpg', './assets/instructions/play/ezgif-frame-035.jpg', './assets/instructions/play/ezgif-frame-036.jpg', './assets/instructions/play/ezgif-frame-037.jpg', './assets/instructions/play/ezgif-frame-038.jpg', './assets/instructions/play/ezgif-frame-039.jpg', './assets/instructions/play/ezgif-frame-040.jpg', './assets/instructions/play/ezgif-frame-041.jpg', './assets/instructions/play/ezgif-frame-042.jpg', './assets/instructions/play/ezgif-frame-043.jpg', './assets/instructions/play/ezgif-frame-044.jpg', './assets/instructions/play/ezgif-frame-045.jpg', './assets/instructions/play/ezgif-frame-046.jpg', './assets/instructions/play/ezgif-frame-047.jpg', './assets/instructions/play/ezgif-frame-048.jpg', './assets/instructions/play/ezgif-frame-049.jpg', './assets/instructions/play/ezgif-frame-050.jpg', './assets/instructions/play/ezgif-frame-051.jpg', './assets/instructions/play/ezgif-frame-052.jpg', './assets/instructions/play/ezgif-frame-053.jpg', './assets/instructions/play/ezgif-frame-054.jpg', './assets/instructions/play/ezgif-frame-055.jpg', './assets/instructions/play/ezgif-frame-056.jpg', './assets/instructions/play/ezgif-frame-057.jpg', './assets/instructions/play/ezgif-frame-058.jpg', './assets/instructions/play/ezgif-frame-059.jpg', './assets/instructions/play/ezgif-frame-060.jpg', './assets/instructions/play/ezgif-frame-061.jpg', './assets/instructions/play/ezgif-frame-062.jpg', './assets/instructions/play/ezgif-frame-063.jpg', './assets/instructions/play/ezgif-frame-064.jpg', './assets/instructions/play/ezgif-frame-065.jpg', './assets/instructions/play/ezgif-frame-066.jpg', './assets/instructions/play/ezgif-frame-067.jpg', './assets/instructions/play/ezgif-frame-068.jpg', './assets/instructions/play/ezgif-frame-069.jpg', './assets/instructions/play/ezgif-frame-070.jpg', './assets/instructions/play/ezgif-frame-071.jpg', './assets/instructions/play/ezgif-frame-072.jpg', './assets/instructions/play/ezgif-frame-073.jpg', './assets/instructions/play/ezgif-frame-074.jpg', './assets/instructions/play/ezgif-frame-075.jpg', './assets/instructions/play/ezgif-frame-076.jpg', './assets/instructions/play/ezgif-frame-077.jpg', './assets/instructions/play/ezgif-frame-078.jpg', './assets/instructions/play/ezgif-frame-079.jpg', './assets/instructions/play/ezgif-frame-080.jpg', './assets/instructions/play/ezgif-frame-081.jpg', './assets/instructions/play/ezgif-frame-082.jpg', './assets/instructions/play/ezgif-frame-083.jpg', './assets/instructions/play/ezgif-frame-084.jpg', './assets/instructions/play/ezgif-frame-085.jpg', './assets/instructions/play/ezgif-frame-086.jpg', './assets/instructions/play/ezgif-frame-087.jpg', './assets/instructions/play/ezgif-frame-088.jpg', './assets/instructions/play/ezgif-frame-089.jpg', './assets/instructions/play/ezgif-frame-090.jpg', './assets/instructions/play/ezgif-frame-091.jpg', './assets/instructions/play/ezgif-frame-092.jpg', './assets/instructions/play/ezgif-frame-093.jpg', './assets/instructions/play/ezgif-frame-094.jpg', './assets/instructions/play/ezgif-frame-095.jpg', './assets/instructions/play/ezgif-frame-096.jpg', './assets/instructions/play/ezgif-frame-097.jpg', './assets/instructions/play/ezgif-frame-098.jpg', './assets/instructions/play/ezgif-frame-099.jpg', './assets/instructions/play/ezgif-frame-100.jpg', './assets/instructions/play/ezgif-frame-101.jpg', './assets/instructions/play/ezgif-frame-102.jpg', './assets/instructions/play/ezgif-frame-103.jpg', './assets/instructions/play/ezgif-frame-104.jpg', './assets/instructions/play/ezgif-frame-105.jpg', './assets/instructions/play/ezgif-frame-106.jpg', './assets/instructions/play/ezgif-frame-107.jpg', './assets/instructions/play/ezgif-frame-108.jpg', './assets/instructions/play/ezgif-frame-109.jpg', './assets/instructions/play/ezgif-frame-110.jpg', './assets/instructions/play/ezgif-frame-111.jpg', './assets/instructions/play/ezgif-frame-112.jpg', './assets/instructions/play/ezgif-frame-113.jpg', './assets/instructions/play/ezgif-frame-114.jpg', './assets/instructions/play/ezgif-frame-115.jpg', './assets/instructions/play/ezgif-frame-116.jpg', './assets/instructions/play/ezgif-frame-117.jpg', './assets/instructions/play/ezgif-frame-118.jpg', './assets/instructions/play/ezgif-frame-119.jpg', './assets/instructions/play/ezgif-frame-120.jpg', './assets/instructions/play/ezgif-frame-121.jpg', './assets/instructions/play/ezgif-frame-122.jpg', './assets/instructions/play/ezgif-frame-123.jpg', './assets/instructions/play/ezgif-frame-124.jpg', './assets/instructions/play/ezgif-frame-125.jpg', './assets/instructions/play/ezgif-frame-126.jpg', './assets/instructions/play/ezgif-frame-127.jpg', './assets/instructions/play/ezgif-frame-128.jpg', './assets/instructions/play/ezgif-frame-129.jpg', './assets/instructions/play/ezgif-frame-130.jpg', './assets/instructions/play/ezgif-frame-131.jpg', './assets/instructions/play/ezgif-frame-132.jpg', './assets/instructions/play/ezgif-frame-133.jpg', './assets/instructions/play/ezgif-frame-134.jpg', './assets/instructions/play/ezgif-frame-135.jpg', './assets/instructions/play/ezgif-frame-136.jpg', './assets/instructions/play/ezgif-frame-137.jpg', './assets/instructions/play/ezgif-frame-138.jpg', './assets/instructions/play/ezgif-frame-139.jpg', './assets/instructions/play/ezgif-frame-140.jpg', './assets/instructions/play/ezgif-frame-141.jpg', './assets/instructions/play/ezgif-frame-142.jpg', './assets/instructions/play/ezgif-frame-143.jpg', './assets/instructions/play/ezgif-frame-144.jpg', './assets/instructions/play/ezgif-frame-145.jpg', './assets/instructions/play/ezgif-frame-146.jpg', './assets/instructions/play/ezgif-frame-147.jpg', './assets/instructions/play/ezgif-frame-148.jpg', './assets/instructions/play/ezgif-frame-149.jpg', './assets/instructions/play/ezgif-frame-150.jpg', './assets/instructions/play/ezgif-frame-151.jpg', './assets/instructions/play/ezgif-frame-152.jpg', './assets/instructions/play/ezgif-frame-153.jpg', './assets/instructions/play/ezgif-frame-154.jpg', './assets/instructions/play/ezgif-frame-155.jpg', './assets/instructions/play/ezgif-frame-156.jpg', './assets/instructions/play/ezgif-frame-157.jpg', './assets/instructions/play/ezgif-frame-158.jpg', './assets/instructions/play/ezgif-frame-159.jpg', './assets/instructions/play/ezgif-frame-160.jpg', './assets/instructions/play/ezgif-frame-161.jpg', './assets/instructions/play/ezgif-frame-162.jpg', './assets/instructions/play/ezgif-frame-163.jpg', './assets/instructions/play/ezgif-frame-164.jpg', './assets/instructions/play/ezgif-frame-165.jpg', './assets/instructions/play/ezgif-frame-166.jpg', './assets/instructions/play/ezgif-frame-167.jpg', './assets/instructions/play/ezgif-frame-168.jpg', './assets/instructions/play/ezgif-frame-169.jpg', './assets/instructions/play/ezgif-frame-170.jpg', './assets/instructions/play/ezgif-frame-171.jpg', './assets/instructions/play/ezgif-frame-172.jpg', './assets/instructions/play/ezgif-frame-173.jpg', './assets/instructions/play/ezgif-frame-174.jpg', './assets/instructions/play/ezgif-frame-175.jpg', './assets/instructions/play/ezgif-frame-176.jpg', './assets/instructions/play/ezgif-frame-177.jpg', './assets/instructions/play/ezgif-frame-178.jpg', './assets/instructions/play/ezgif-frame-179.jpg', './assets/instructions/play/ezgif-frame-180.jpg', './assets/instructions/play/ezgif-frame-181.jpg', './assets/instructions/play/ezgif-frame-182.jpg', './assets/instructions/play/ezgif-frame-183.jpg', './assets/instructions/play/ezgif-frame-184.jpg', './assets/instructions/play/ezgif-frame-185.jpg', './assets/instructions/play/ezgif-frame-186.jpg', './assets/instructions/play/ezgif-frame-187.jpg', './assets/instructions/play/ezgif-frame-188.jpg', './assets/instructions/play/ezgif-frame-189.jpg', './assets/instructions/play/ezgif-frame-190.jpg', './assets/instructions/play/ezgif-frame-191.jpg', './assets/instructions/play/ezgif-frame-192.jpg', './assets/instructions/play/ezgif-frame-193.jpg', './assets/instructions/play/ezgif-frame-194.jpg', './assets/instructions/play/ezgif-frame-195.jpg', './assets/instructions/play/ezgif-frame-196.jpg', './assets/instructions/play/ezgif-frame-197.jpg', './assets/instructions/play/ezgif-frame-198.jpg', './assets/instructions/play/ezgif-frame-199.jpg', './assets/instructions/play/ezgif-frame-200.jpg']),
    ('assets/music', [
        'assets/music/bgm.mp3',
        'assets/music/button.mp3',
        'assets/music/traffic.mp3',
    ]),
    ('assets/sign', [
        'assets/sign/cross.png',
        'assets/sign/bz.png',
        'assets/sign/shovel.png',
        'assets/sign/settings.png',
        'assets/sign/instructions.png',
    ]),
    ('assets/title', [
        'assets/title/diffTitle.png',
        'assets/title/diffLevel.png',
        'assets/title/history.png',
        'assets/title/username.png',
        'assets/title/title.png'
    ]),

]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['cmu_graphics', 'PIL', 'objects', 'practicalFunctions','math'],
    'includes': ['cmu_graphics', 'PIL', 'objects', 'practicalFunctions','math'],
    'iconfile': 'assets/sign/cross.png',  # Preferably use a .icns file for macOS icons
    'plist': {
        'CFBundleName': 'TimeWiseTransport',
        'CFBundleDisplayName': 'TimeWise Transport',
        'CFBundleIdentifier': 'com.yourdomain.timewisetransport',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'LSUIElement': False,
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
