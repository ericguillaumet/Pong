for r in rackets:
            if self.right >= r.left and\
                self.left <= r.right and\
                self.down >= r.up and\
                self.up <= r.down:
                    self.vx *= -1
                    break

