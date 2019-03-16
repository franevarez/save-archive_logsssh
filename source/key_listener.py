class _GetCh:
  def __init__(self):
    try:
      self.impl = _GetChWindows()
    except ImportError:
      try:
        self.impl = _GetChMacCarbon()
      except ImportError:
        self.impl = _GetChUnix()

  def __call__(self):
    return self.impl()


class _GetChWindows:
  def __init__(self):
    import msvcrt

  def __call__(self):
    import msvcrt
    if msvcrt.kbhit():
      while msvcrt.kbhit():
        ch = msvcrt.getch()
      while ch in b'\x00\xe0':
        msvcrt.getch()
        ch = msvcrt.getch()
      return ord(ch.decode())
    else:
      return -1


class _GetChMacCarbon:
  def __init__(self):
    import Carbon
    Carbon.Evt

  def __call__(self):
    import Carbon
    if Carbon.Evt.EventAvail(0x0008)[0] == 0:  # 0x0008 is the keyDownMask
      return ""
    else:
      (what, msg, when, where, mod) = Carbon.Evt.GetNextEvent(0x0008)[1]
      return msg & 0x000000FF


class _GetChUnix:
  def __init__(self):
    import tty
    import sys
    import termios  # import termios now or else you'll get the Unix
    # version on the Mac

  def __call__(self):
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ord(ch)
