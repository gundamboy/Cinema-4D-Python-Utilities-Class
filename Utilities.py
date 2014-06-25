class HelperUtils(object):
    """Several helper methods"""

    def __init__(self, arg):
        super(Utilities, self).__init__()

        @staticmethod
    def hu_open_website(website):
        """Open default web browser and route to plugin Website

        :param string website: the full url to the site
        """

        webbrowser.open(website)

    @staticmethod
    def hu_about(plugin_title, version, coyright_year, author, website):
        """Show About information dialog box

        :param string plugin_title: name of plugin
        :param string version: version
        :param string copyright_year: year created
        :param string author: author of plugin
        :param string website: the website url
        """

        gui.MessageDialog("{0} v{1}\nCopyright (C) {2} {3}.\nAll rights reserved.\n\n{4}\n\n".format(plugin_title, version, copyright_year, author, website), c4d.GEMB_OK)


    @staticmethod
    def hu_get_timedelta(time_a, time_b):
        """Get difference between two timestamps.

        :param datetime tima_a: datetime object start time
        :param datetime tima_b: datetime object end time
        :return tuple: elapsed time
        """

        time_d = time_b - time_a
        days = time_d.days
        hours, remainder = divmod(time_d.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        return (days, hours, minutes, seconds)


    @staticmethod
    def hu_get_activeDoc():
        """Returns doc object"""

        activeDoc = documents.GetActiveDocument()

        return(activeDoc)


    @staticmethod
    def hu_get_activeDocPath():
        """Return the document path without scene name"""

        activeDoc = documents.GetActiveDocument()
        activeDocPath = activeDoc.GetDocumentPath()

        return(activeDocPath)

    @staticmethod
    def hu_get_activeDocName():
        """Return the document name without extension"""

        activeDoc = documents.GetActiveDocument()
        activeDocName = activeDoc.GetDocumentName()

        return(activeDocName)

    @staticmethod
    def hu_get_fullActiveDocName():
        """Return the document name with extension"""

        activeDoc = documents.GetActiveDocument()
        activeDocName = activeDoc.GetDocumentName()

        fullActiveDocName = activeDocName + ".c4d"

        return(fullActiveDocName)

    @staticmethod
    def hu_hasExpired(year, month, day, hour, minutes):
        """Check if date and time has passed

        :param int year: 2014
        :param int month: 1
        :param int day: 10
        :param int hour: 12
        :param int minutes: 30
        :return bool: False or True
        """

        expired = datetime.datetime(year, month, day, hour, minutes)

        if datetime.datetime.now() > expired:
            return(True)
        else:
            return(False)

    @staticmethod
    def hu_get_layers_root():
        """Returns document layers"""
        activeDoc = documents.GetActiveDocument()
        root = activeDoc.GetLayerObjectRoot()

        return(root)

    @staticmethod
    def hu_get_layers():
        """Returns document layers"""
        activeDoc = documents.GetActiveDocument()
        root = activeDoc.GetLayerObjectRoot()
        layers = root.GetChildren()

        return(layers)

    @staticmethod
    def hu_random_number():
        num = random.randrange(0,10000)

        return(num)

    @staticmethod   
    def hu_GetNextObject(op):
        if op==None: return None
        if op.GetDown(): return op.GetDown()
        while not op.GetNext() and op.GetUp():
            op = op.GetUp()
        return op.GetNext()

    @staticmethod
    def hu_GetAllObjects():
        activeDoc = documents.GetActiveDocument()
        op = activeDoc.GetFirstObject()
        allobjs = []

        while op:
            allobjs.append(op)
            op = HelperUtils.GetNextObject(op)

        return allobjs