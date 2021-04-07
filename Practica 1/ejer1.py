variable1 = """NumPy is the fundamental package needed for scientific computing with Python. \n

Website: https://www.numpy.org \n
Documentation: https://numpy.org/doc\n
Mailing list: http://mail.python.org/mailman/listinfo/numpy-discussion \n
Source code: https://github.com/numpy/numpy\n
Contributing: http://www.numpy.org/devdocs/dev/index.html \n
Bug reports: https://github.com/numpy/numpy/issues\n
It provides:\n

a powerful N-dimensional array object\n
sophisticated (broadcasting) functions\n
tools for integrating C/C++ and Fortran code\n
useful linear algebra, Fourier transform, and random number capabilities\n
Testing:\n
http
NumPy requires pytest. Tests can then be run after installation with:\n

python -c 'import numpy; numpy.test()'\n
Call for Contributions\n
The NumPy project welcomes your expertise and enthusiasm!\n

Small improvements or fixes are always appreciated; issues labeled as "good first issue" may be a good starting point. If you are considering larger contributions to the source code, please contact us through the mailing list first.\n

Writing code isn’t the only way to contribute to NumPy. You can also:\n

review pull requests\n
triage issues\n
develop tutorials, presentations, and other educational materials\n
maintain and improve our website\n
develop graphic design for our brand assets and promotional materials\n
translate website content\n
help with outreach and onboard new contributors\n
write grant proposallss and help with other fundraising efforts\n
If you’re unsure where to start or how your skills fit in, reach out! You can ask on the mailing list or here, on GitHub, by opening a new issue or leaving a comment on a relevant issue that is already open.\n
\n
Our preferred channels of communication are all public, but if you’d like to speak to us in private first, contact our community coordinators at numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for an invite).\n

We also have a biweekly community call, details of which are announced on the mailing list. You are very welcome to join.\n

If you are new to contributing to open source, this guide helps explain why, what, and how to successfully get involved.\n"""

listaTransformada = variable1.split("\n")
https = 0
http = 0
for dev in listaTransformada:
    if ("https" in dev):
        https = https + 1
    elif  ("http" in dev):
        http = http + 1

print ("Se leyo {} lineas con http y {} con  https" .format(http,https))
