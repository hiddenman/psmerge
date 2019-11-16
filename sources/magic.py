featurebegin='%%BeginFeature: ';
featureend='%%EndFeature';
psprolog=[
    '%!PS\n',
    '/_begin_job_\n',
    '{\n',
    '   /tweak_save save def\n',
    '   /tweak_dc countdictstack def\n',
    '   /tweak_oc count 1 sub def\n',
    '   userdict begin\n',
    '}bind def\n',
    '\n',
    '/_end_job_\n',
    '{\n',
    '   count tweak_oc sub{pop}repeat\n',
    '   countdictstack tweak_dc sub{end}repeat\n',
    '   tweak_save restore\n',
    '}bind def\n'
    ];

staple={
    'none':
    {'name':'*KOStapleLocation None',
     'cmd1':'<< /StapleMode (Off) >>',
     'cmd2':'/KonicaOptions /ProcSet findresource /setkonicaoptions get exec'
     },
    'singleportrait':
    {'name':'*KOStapleLocation SinglePortrait',
     'cmd1':'<< /StapleMode (SinglePortrait) >>',
     'cmd2':'/KonicaOptions /ProcSet findresource /setkonicaoptions get exec'
     },
    'singlelandscape':
    {'name':'*KOStapleLocation SingleLandscape',
     'cmd1':'<< /StapleMode (SingleLandscape) >>',
     'cmd2':'/KonicaOptions /ProcSet findresource /setkonicaoptions get exec'
     },
    'doublesideportrait':
    {'name':'*KOStapleLocation DualPortrait',
     'cmd1':'<< /StapleMode (DoubleSidePortrait) >>',
     'cmd2':'/KonicaOptions /ProcSet findresource /setkonicaoptions get exec'
     },
    'doublesidelandscape':
    {'name':'*KOStapleLocation DualLandscape',
     'cmd1':'<< /StapleMode (DoubleSideLandscape) >>',
     'cmd2':'/KonicaOptions /ProcSet findresource /setkonicaoptions get exec'
     },
    'doubletopportrait':
    {'name':'*KOStapleLocation DualPortraitTop',
     'cmd1':'<< /StapleMode (DoubleTopPortrait) >>',
     'cmd2':'/KonicaOptions /ProcSet findresource /setkonicaoptions get exec'
     },
    'doubletoplandscape':
    {'name':'*KOStapleLocation DualLandscapeTop',
     'cmd1':'<< /StapleMode (DoubleTopLandscape) >>',
     'cmd2':'/KonicaOptions /ProcSet findresource /setkonicaoptions get exec'
     }
    }

duplex={
    'none':
    {'name':'*Duplex None',
     'cmd1':'<< /Duplex false /Tumble false >> setpagedevice',
     'cmd2':''
     },
    'longedge':
    {'name':'*Duplex DuplexNoTumble',
     'cmd1':'<< /Duplex true /Tumble false >> setpagedevice',
     'cmd2':''
     },
    'shortedge':
    {'name':'*Duplex DuplexTumble',
     'cmd1':'<< /Duplex true /Tumble true >> setpagedevice',
     'cmd2':''
     }
    };

outtray={
    'none':
    {
    'name':'*OutputBin None',
    'cmd1':'<</OutputType (DEFAULT)>> setpagedevice',
    'cmd2':''
    },
    'tray1':
    {'name':'*OutputBin Bin1',
     'cmd1':'<</OutputType (BIN1)>> setpagedevice',
     'cmd2':''
     },
    'tray2':
    {'name':'*OutputBin Bin2',
     'cmd1':'<</OutputType (BIN2)>> setpagedevice',
     'cmd2':''
     },
    'tray3':
    {'name':'*OutputBin Bin3',
     'cmd1':'<</OutputType (BIN3)>> setpagedevice',
     'cmd2':''
     }
    };

