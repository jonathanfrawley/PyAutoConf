class Redshift:
    def __init__(self, redshift=0.0):
        self.redshift = redshift


class SphProfile:
    def __init__(self, centre=(0.0, 0.0)):
        """ Generic circular profiles class to contain functions shared by light and
        mass profiles.

        Parameters
        ----------
        centre: (float, float)
            The (y,x) coordinates of the origin of the profile.
        """
        self.centre = centre


class EllProfile(SphProfile):
    def __init__(self, centre=(0.0, 0.0), axis_ratio=1.0, phi=0.0):
        """ Generic elliptical profiles class to contain functions shared by light
        and mass profiles.

        Parameters
        ----------
        centre: (float, float)
            The (y,x) coordinates of the origin of the profiles
        axis_ratio : float
            Ratio of profiles ellipse's minor and major axes (b/a)
        phi : float
            Rotational angle of profiles ellipse counter-clockwise from positive x-axis
        """
        super(EllProfile, self).__init__(centre)
        self.axis_ratio = axis_ratio
        self.phi = phi


class EllGaussian(EllProfile):
    def __init__(
            self, centre=(0.0, 0.0), axis_ratio=1.0, phi=0.0, intensity=0.1, sigma=0.01
    ):
        """ The elliptical Gaussian profile.

        Parameters
        ----------
        centre: (float, float)
            The (y,x) origin of the light profile.
        axis_ratio : float
            Ratio of light profiles ellipse's minor and major axes (b/a).
        phi : float
            Rotation angle of light profile counter-clockwise from positive x-axis.
        intensity : float
            Overall intensity normalisation of the light profiles (electrons per
            second).
        sigma : float
            The full-width half-maximum of the Gaussian.
        """
        super(EllGaussian, self).__init__(centre, axis_ratio, phi)

        self.intensity = intensity
        self.sigma = sigma
