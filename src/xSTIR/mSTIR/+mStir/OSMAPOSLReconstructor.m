classdef OSMAPOSLReconstructor < mStir.IterativeReconstructor
%     Class for reconstructor objects using Ordered Subsets Maximum A Posteriori 
%     One Step Late reconstruction algorithm, see
%     http://stir.sourceforge.net/documentation/doxy/html/classstir_1_1OSMAPOSLReconstruction.html
    properties
        name
    end
    methods
        function self = OSMAPOSLReconstructor(filename)
            self.name = 'OSMAPOSL';
            if nargin < 1
                filename = '';
            end
            self.handle = calllib...
                ('mstir', 'mSTIR_objectFromFile',...
                'OSMAPOSLReconstruction', filename);
            mUtil.checkExecutionStatus(self.name, self.handle);
        end
        function delete(self)
            calllib('mutilities', 'mDeleteDataHandle', self.handle)
            self.handle = [];
        end
        function set_MAP_model(self, model)
            mStir.setParameter(self.handle, self.name, 'MAP_model', model, 'c')
        end
        function obj_fun = get_objective_function(self)
            obj_fun = mStir.PoissonLogLh_LinModMean();
            obj_fun.handle = calllib('mstir', 'mSTIR_parameter',...
                self.handle, self.name, 'objective_function');
            mUtil.checkExecutionStatus...
                ([self.name ':get_objective_function'], obj_fun.handle)
        end
    end
end
