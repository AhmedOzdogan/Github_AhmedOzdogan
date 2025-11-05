interface FormContainerProps {
    title?: string;
    children?: React.ReactNode;
}

function FormContainer({ title, children }: FormContainerProps) {
    return (
        <div className="flex justify-center items-center min-h-screen bg-gray-100">
            <div className="bg-white shadow-md rounded-xl p-8 w-full max-w-md">
                {title && (
                    <h2 className="text-2xl font-semibold text-center mb-6 text-gray-800">
                        {title}
                    </h2>
                )}
                {children}
            </div>
        </div>
    );
}

export default FormContainer;
