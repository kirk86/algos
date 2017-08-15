from scipy import zeros, asarray, sign, array, cov, dot, clip, ndarray
from scipy.linalg import inv
from keras.optimizers import Optimizer
from keras import backend as K


class GradientDescent(Optimizer):
    def __init__(self, alpha=0.1, alphadecay=1.0, momentum=0.,
                 momentumvector=None, rprop=False, deltamax=5.0,
                 deltamin=0.01, deltanull=0.1, etaplus=1.2,
                 etaminus=0.5, lastgradient=None, **kwargs):
        """ initialize algorithms with standard parameters
            (typical values given in parentheses)"""

        super(GradientDescent, self).__init__(**kwargs)

        with K.name_scope(self.__class__.__name__):
            self.iterations = K.variable(0., name='iterations')
            self.alpha = K.variable(alpha, name='alpha')
            self.alphadecay = K.variable(alphadecay, name='alphadecay')
            self.momentum = K.variable(momentum, name='momentum')
            self.deltamax = K.variable(deltamax, name='deltamax')
            self.deltamin = K.variable(deltamin, name='deltamin')
            self.deltanull = K.variable(deltanull, name='deltanull')
            self.etaplus = K.variable(etaplus, name='etaplus')
            self.etaminus = K.variable(etaminus, name='etaminus')
            # self.decay = K.variable(decay, name='decay')
        # --- BackProp parameters ---
        # learning rate (0.1-0.001, down to 1e-7 for RNNs)
        self.alpha = alpha

        # alpha decay (0.999; 1.0 = disabled)
        self.alphadecay = alphadecay

        # momentum parameters (0.1 or 0.9)
        self.momentum = momentum
        self.momentumvector = momentumvector

        # --- RProp parameters ---
        self.rprop = rprop
        # maximum step width (1 - 20)
        self.deltamax = deltamax
        # minimum step width (0.01 - 1e-6)
        self.deltamin = deltamin

        # the remaining parameters do not normally need to be changed
        self.deltanull = deltanull
        self.etaplus = etaplus
        self.etaminus = etaminus
        self.lastgradient = lastgradient

    def init(self, values):
        """ call this to initialize data structures to use *after* algorithm
        has been selected
        :arg values: the list (or array) of parameters to perform gradient
         descent on
        (will be copied, original not modified)
        """
        assert isinstance(values, ndarray)
        self.values = values.copy()
        if self.rprop:
            self.lastgradient = zeros(len(values), dtype='float64')
            self.rprop_theta = self.lastgradient + self.deltanull
            self.momentumvector = None
        else:
            self.lastgradient = None
            self.momentumvector = zeros(len(values))

    def __call__(self, gradient, error=None):
        """ calculates parameter change based on given gradient and returns
            updated parameters
            check if gradient has correct dimensionality, then make array """
        assert len(gradient) == len(self.values)
        gradient_arr = asarray(gradient)

        if self.rprop:
            rprop_theta = self.rprop_theta

            # update parameters
            self.values += sign(gradient_arr) * rprop_theta

            # update rprop meta parameters
            dirSwitch = self.lastgradient * gradient_arr
            rprop_theta[dirSwitch > 0] *= self.etaplus
            idx =  dirSwitch < 0
            rprop_theta[idx] *= self.etaminus
            gradient_arr[idx] = 0

            # upper and lower bound for both matrices
            rprop_theta = rprop_theta.clip(min=self.deltamin, max=self.deltamax)

            # save current gradients to compare with in next time step
            self.lastgradient = gradient_arr.copy()

            self.rprop_theta = rprop_theta

        else:
            # update momentum vector (momentum = 0 clears it)
            self.momentumvector *= self.momentum
            # update parameters (including momentum)
            self.momentumvector += self.alpha * gradient_arr
            self.alpha *= self.alphadecay

            # update parameters
            self.values += self.momentumvector

        return self.values
